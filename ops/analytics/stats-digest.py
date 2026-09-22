#!/usr/bin/env python3
"""Generate and publish the weekly digest. Human-Curated, AI-Enabled (HCAE)."""
import argparse
import datetime as dt
import fcntl
import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import urllib.parse

spec = importlib.util.spec_from_file_location('weekly_report', Path(__file__).with_name('weekly-report.py'))
weekly = importlib.util.module_from_spec(spec)
spec.loader.exec_module(weekly)
TARGET = 'ops/analytics/stats-weekly.md'
REPO = 'https://github.com/jdlongmire/thinx-tank.git'


def metrics(start, end, kind, token):
    query = urllib.parse.urlencode({'startAt':int(start.timestamp()*1000), 'endAt':int(end.timestamp()*1000)-1, 'type':kind, 'limit':10})
    result = weekly.request(f'http://127.0.0.1:19880/api/websites/{weekly.WEBSITE}/metrics?{query}', token=token)
    if not isinstance(result, list):
        raise ValueError('Invalid metrics response')
    rows = []
    for row in result:
        if not isinstance(row, dict) or not isinstance(row.get('x'), str) or not isinstance(row.get('y'), (int, float)) or row['y'] < 0:
            raise ValueError('Invalid metrics row')
        rows.append((row['x'], row['y']))
    return sorted(rows, key=lambda r:(-r[1], r[0]))[:10]


def cell(value):
    # Analytics fields are untrusted visitor input; keep a stable Markdown table.
    return str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', '&#124;').replace('\r', ' ').replace('\n', ' ')


def render(start, end, generated, totals, pages, referrers, days):
    if len(days) != 7 or sum(n for _, n in days) != totals['pageviews']:
        raise ValueError('Daily pageviews do not reconcile with total')
    last = (end-dt.timedelta(days=1)).date()
    lines = ['# Thinx-Tank weekly stats', '', 'Format version: 1', f'Week start: {start.date()}', f'Week end: {last}', 'Timezone: America/Chicago', f'Generated at: {generated.isoformat(timespec="seconds")}', 'Website: blog.thinxai.net', '']
    if start < weekly.STARTED:
        lines += ['Coverage: Tracking began 2026-09-21; earlier dates have no coverage. Zero counts before that date do not establish zero traffic.', '']
    elif start.date() == weekly.STARTED.date():
        lines += ['Coverage: Partial coverage on deployment day (2026-09-21); includes setup verification visits.', '']
    else:
        lines += ['Coverage: Recorded events only; tracking outages and blocked tracking may reduce counts.', '']
    lines += ['## Totals', '', '| Metric | Count |', '| --- | ---: |']
    lines += [f'| {label} | {totals[key]} |' for label,key in [('Pageviews','pageviews'),('Unique visitors','visitors'),('Visits','visits')]]
    for title,label,rows in [('Top 10 pages','Path',pages),('Top 10 referrers','Referrer',referrers)]:
        lines += ['', '## '+title, '', f'| {label} | Views |', '| --- | ---: |']
        lines += [f'| {cell(x or "(direct / none)")} | {y} |' for x,y in rows] or ['| (no recorded data) | 0 |']
    lines += ['', '## Day-by-day pageviews', '', '| Date | Pageviews |', '| --- | ---: |']
    lines += [f'| {date} | {n} |' for date,n in days]
    return '\n'.join(lines)+'\n\nHuman-Curated, AI-Enabled (HCAE)\n'


def generate(now):
    start, end = weekly.period(now)
    creds = weekly.env_file(Path.home()/'.config/thinx/analytics/admin.env')
    auth = weekly.request('http://127.0.0.1:19880/api/auth/login', {'username':creds['UMAMI_USERNAME'], 'password':creds['UMAMI_PASSWORD']})
    token = auth['token']
    totals = weekly.stats(start, end, token)
    # Umami 3.4 renamed the spec's URL metric to path.
    pages = metrics(start, end, 'path', token)
    referrers = metrics(start, end, 'referrer', token)
    days = []
    for i in range(7):
        day = start+dt.timedelta(days=i)
        days.append((day.date(), weekly.stats(day, day+dt.timedelta(days=1), token)['pageviews']))
    return render(start, end, now, totals, pages, referrers, days)


def publish(content):
    # Fresh checkout isolates the scheduled writer from human/theme development.
    with tempfile.TemporaryDirectory(prefix='thinx-digest-') as directory:
        def git(*args):
            return subprocess.run(['git', '-C', directory, *args], check=True, capture_output=True, text=True).stdout
        subprocess.run(['git', 'clone', '--quiet', '--depth=1', '--branch=main', '--single-branch', REPO, directory], check=True, capture_output=True)
        target = Path(directory)/TARGET
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
        git('add', '--', TARGET)
        if not git('diff', '--cached', '--name-only').strip():
            print('Digest already current')
            return
        git('commit', '-m', 'Update weekly Thinx-Tank traffic digest', '-m', 'Human-Curated, AI-Enabled (HCAE)')
        expected = git('rev-parse', 'HEAD').strip()
        # Normal fast-forward push only; concurrent main updates fail safely.
        git('push', 'origin', 'HEAD:main')
        observed = git('ls-remote', 'origin', 'refs/heads/main').split()[0]
        if observed != expected:
            raise RuntimeError('Remote advanced during publication verification')
        print('Published digest:', expected)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--publish', action='store_true')
    args = parser.parse_args()
    os.umask(0o077)
    state = Path.home()/'.local/share/thinx-tank-analytics/reports'
    state.mkdir(parents=True, exist_ok=True)
    with (state/'digest.lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        content = generate(dt.datetime.now(weekly.TZ))
        if args.publish:
            publish(content)
        else:
            print(content, end='')

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('Stats digest failed:', type(exc).__name__)
        raise SystemExit(1)
