#!/usr/bin/env python3
"""Weekly Thinx-Tank report. Human-Curated, AI-Enabled (HCAE)."""
import argparse
import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import urllib.request
from zoneinfo import ZoneInfo

TZ = ZoneInfo('America/Chicago')
WEBSITE = 'b7cfc1ca-94d3-43a8-8e7e-e3772603d806'
CHAT = '6996242753'
STARTED = dt.datetime(2026, 9, 21, tzinfo=TZ)
BRIDGE_ENV = Path('/data/thinx-home/principals/thinxai/thinx-home/05-mxm-construct/means/services/telegram-bridge/.env')


def env_file(path):
    result = {}
    for line in path.read_text().splitlines():
        if line.strip() and not line.lstrip().startswith('#') and '=' in line:
            key, value = line.split('=', 1)
            result[key.strip()] = value.strip().strip('\"\'')
    return result


def request(url, body=None, token=None):
    headers = {'Content-Type': 'application/json'}
    if token:
        headers['Authorization'] = 'Bearer ' + token
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def period(now):
    local = now.astimezone(TZ)
    end = local.replace(hour=0, minute=0, second=0, microsecond=0) - dt.timedelta(days=local.weekday())
    return end - dt.timedelta(days=7), end


def stats(start, end, token):
    # Inclusive API end timestamp; calendar arithmetic above preserves local DST boundaries.
    a, b = int(start.timestamp() * 1000), int(end.timestamp() * 1000) - 1
    data = request(f'http://127.0.0.1:19880/api/websites/{WEBSITE}/stats?startAt={a}&endAt={b}', token=token)
    for key in ('pageviews', 'visitors', 'visits'):
        if not isinstance(data.get(key), (int, float)):
            raise ValueError('Invalid analytics response')
    return data


def change(value, prior):
    if prior == 0:
        return 'no prior traffic' if value else 'unchanged'
    return f'{(value-prior)/prior:+.0%}'


def report(start, end, current, previous, test=False):
    last_day = (end - dt.timedelta(microseconds=1)).date()
    lines = ['THINX-TANK — ' + ('TEST REPORT (week to date)' if test else 'WEEKLY STATS'),
             f'{start:%b %d}–{last_day:%b %d, %Y} · America/Chicago', '']
    for label, key in [('Pageviews', 'pageviews'), ('Visitors', 'visitors'), ('Visits', 'visits')]:
        suffix = '' if test or start < STARTED + dt.timedelta(days=7) else f' ({change(current[key], previous[key])} vs prior week)'
        lines.append(f'{label}: {current[key]:,}{suffix}')
    if start < STARTED:
        lines.append('\nTracking began Sep 21, 2026; earlier dates have no coverage.')
    elif start.date() == STARTED.date():
        lines.append('\nFirst week: partial coverage from Sep 21 deployment; includes setup verification visits.')
    lines.append('\nhttps://blog.thinxai.net')
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--send', action='store_true')
    parser.add_argument('--test', action='store_true', help='Send a labeled week-to-date test without consuming weekly delivery')
    args = parser.parse_args()
    os.umask(0o077)
    state = Path.home()/'.local/share/thinx-tank-analytics/reports'
    state.mkdir(parents=True, exist_ok=True)
    with (state/'lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        now = dt.datetime.now(TZ)
        start, end = period(now)
        if args.test:
            start, end = end, now
        key = start.date().isoformat()
        sent = state/f'{key}.json'
        if args.send and not args.test and sent.exists():
            print('Report already delivered for', key)
            return
        creds = env_file(Path.home()/'.config/thinx/analytics/admin.env')
        auth = request('http://127.0.0.1:19880/api/auth/login', {'username':creds['UMAMI_USERNAME'], 'password':creds['UMAMI_PASSWORD']})
        current = stats(start, end, auth['token'])
        previous = stats(start-dt.timedelta(days=7), start, auth['token'])
        message = report(start, end, current, previous, args.test)
        if not args.send:
            print(message)
            return
        bot = env_file(BRIDGE_ENV)['TELEGRAM_BOT_TOKEN']
        response = request(f'https://api.telegram.org/bot{bot}/sendMessage', {'chat_id':CHAT, 'text':message, 'link_preview_options':{'is_disabled':True}})
        if not response.get('ok'):
            raise RuntimeError('Telegram delivery rejected')
        record = {'period_start':start.isoformat(), 'period_end':end.isoformat(), 'sent_at':now.isoformat(), 'message_id':response['result']['message_id'], 'chat_id':CHAT, 'test':args.test}
        target = state/(f'test-{now:%Y%m%dT%H%M%S}.json') if args.test else sent
        temporary = target.with_suffix('.tmp')
        temporary.write_text(json.dumps(record, indent=2)+'\n')
        temporary.replace(target)
        print('Telegram report delivered; message ID', record['message_id'])

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        # HTTP error URLs can contain the Telegram token; never emit exception text.
        print('Weekly report failed:', type(exc).__name__)
        raise SystemExit(1)
