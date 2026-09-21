import json,time,urllib.request
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path.home()/'.config/thinx/analytics'
v=dict(x.split('=',1) for x in (root/'admin.env').read_text().splitlines())
def api(path,body=None,token=None):
 headers={'Content-Type':'application/json'}
 if token:headers['Authorization']='Bearer '+token
 return json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:19880'+path,data=json.dumps(body).encode() if body is not None else None,headers=headers)))
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 context=browser.new_context(user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
 page=context.new_page()
 responses=[]
 page.on('response',lambda r:responses.append({'url':r.url,'status':r.status}) if 'analytics.thinxai.net' in r.url else None)
 page.goto('https://blog.thinxai.net/?analytics-verification=20260921',wait_until='networkidle')
 page.wait_for_timeout(3000)
 print('Collection responses:',json.dumps(responses))
 assert any(r['url'].endswith('/script.js') and r['status']==200 for r in responses), 'Tracker did not load'
 assert any('/api/send' in r['url'] and r['status']==200 for r in responses), 'Browser pageview was not accepted'
 page.goto('https://thinx-003.tail99d888.ts.net:13443/login',wait_until='networkidle')
 print('Dashboard login page:',page.title())
 page.locator('input[name="username"]').fill(v['UMAMI_USERNAME'])
 page.locator('input[name="password"]').fill(v['UMAMI_PASSWORD'])
 page.locator('button[type="submit"]').click()
 page.wait_for_url('**/websites',timeout=20000)
 page.wait_for_load_state('networkidle')
 print('Authenticated dashboard:', page.title())
 page.get_by_text('Thinx-Tank',exact=True).first.wait_for(timeout=20000)
 print('PASS: registered website visible in authenticated dashboard')
 dnt=browser.new_context(user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
 dnt.add_init_script("Object.defineProperty(navigator, 'doNotTrack', {get: () => '1'})")
 dnt_page=dnt.new_page()
 dnt_requests=[]
 dnt_page.on('request',lambda r:dnt_requests.append(r.url) if 'analytics.thinxai.net/api/send' in r.url else None)
 dnt_page.goto('https://blog.thinxai.net/',wait_until='networkidle')
 dnt_page.wait_for_timeout(2000)
 assert not dnt_requests, 'Do Not Track was ignored'
 print('PASS: Do Not Track prevents collection')
 browser.close()
auth=api('/api/auth/login',{'username':v['UMAMI_USERNAME'],'password':v['UMAMI_PASSWORD']})
now=int(time.time()*1000)
stats=api('/api/websites/b7cfc1ca-94d3-43a8-8e7e-e3772603d806/stats?startAt='+str(now-3600000)+'&endAt='+str(now),token=auth['token'])
print('Authenticated stats:',json.dumps(stats))

assert stats['pageviews'] >= 1, 'No pageviews in authenticated dashboard API'
