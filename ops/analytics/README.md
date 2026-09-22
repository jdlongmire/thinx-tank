# Thinx-Tank analytics operations

Human-Curated, AI-Enabled (HCAE)

## Deployment

Host: thinx-003. Runtime owner: thinxai. Rootless Podman 5.4 Quadlet,
Umami 3.4.0 and PostgreSQL 17 (image digests pinned in the units).
Application cap: 1.5 GiB / 1.5 CPUs; database cap: 768 MiB / 1 CPU.
PostgreSQL uses a named volume and has no published port. Umami binds
127.0.0.1:19880. Linger is enabled so user services run without a login.

Public tracker: https://analytics.thinxai.net/script.js
Website ID: b7cfc1ca-94d3-43a8-8e7e-e3772603d806
Private dashboard: https://thinx-003.tail99d888.ts.net:13443/

The dedicated Cloudflare tunnel allows only `/script.js` and `/api/send`;
all other public paths return 404. Dashboard access requires tailnet access
and an Umami login. No shared dashboard is enabled. PostgreSQL stays inside
the container network. Tracking is enabled only in Hugo production builds,
limited by the browser tracker to blog.thinxai.net, and respects Do Not Track.
Public ingestion is inherently unauthenticated; the domain setting is not
proof of event authenticity. No custom events, replays or heatmaps are enabled.

## Private configuration

Credentials are outside Git, under `~/.config/thinx/analytics/` (0700):
`db.env`, `app.env`, `admin.env` (0600). Admin username: admin. Retrieve the
password locally from admin.env; never paste it into logs or repository files.
Tunnel credentials remain under `~/.cloudflared/`; config contains only their path.

To recreate on this host, pull the pinned images, provision fresh private env
files (POSTGRES_USER/DB/PASSWORD, DATABASE_URL, APP_SECRET and
TWO_FACTOR_ENCRYPTION_KEY), then copy the `.container`, `.network`, and `.volume`
files to `~/.config/containers/systemd/`. Copy services/timer to
`~/.config/systemd/user/`, cloudflared.yml to `~/.config/thinx/analytics/`, and
backup.sh to `~/.local/lib/thinx-tank-analytics/` (executable).
Run `systemctl --user daemon-reload`, start analytics.service, enable/start
analytics-tunnel.service and analytics-backup.timer. Quadlet's Install sections
attach both containers to default.target. Rotate the initial default admin
password before exposing dashboard access. Preserve the existing website ID
when restoring; a fresh registration requires updating hugo.toml.

The tunnel DNS record is analytics.thinxai.net, proxied CNAME to tunnel UUID
659eb886-dcd8-4898-9852-9d70e3ce2b1f.cfargotunnel.com. Pass the explicit
analytics config to cloudflared commands; the default config names a different
tunnel. The private proxy uses `tailscale serve --bg --https=13443
http://127.0.0.1:19880` and does not use Funnel.

## Checks and maintenance

- `systemctl --user status analytics analytics-db analytics-tunnel analytics-backup.timer`
- `podman ps` and `curl --fail http://127.0.0.1:19880/api/heartbeat`
- Public script must return 200; `/`, `/login`, `/api/websites` must return 404.
- Log in through the tailnet dashboard to inspect pageviews.
- Review image upgrades deliberately; take a database backup before migrations.
- Existing console/auth/git services and tunnels are independent of this stack.

## Backups and restoration

Daily at approximately 03:20 host time, the timer writes a PostgreSQL custom dump
and SHA-256 checksum to `~/.local/share/thinx-tank-analytics/backups/`.
Retention: 30 days. Files are private. These are **local backups**, not protection
against loss of the host/disk; off-host replication is not configured.
Run `systemctl --user start analytics-backup.service` for a manual backup.

Before restoration, validate the checksum and restore into a separate database:
`podman exec thinx-tank-analytics-db createdb -U umami restore_check`
then pipe the dump into `podman exec -i thinx-tank-analytics-db pg_restore
-U umami -d restore_check --no-owner --exit-on-error`. Compare website and event
counts before authorizing replacement of the production database.

## Rollback

Remove the production tracker block/config and redeploy Hugo to stop collection.
Stop only analytics-tunnel.service and analytics.service, and disable the backup
timer if retiring the stack. Preserve the database volume and backups. Remove
only this tailnet Serve mapping with `tailscale serve --https=13443 off`.
Do not reset all Serve configuration or touch the console's existing tunnel.

## Weekly Telegram report

JD requested weekly reports to his Telegram DM on 2026-09-21.
`analytics-weekly-report.timer` runs Mondays at 09:00 America/Chicago (DST-aware),
starting September 28, 2026. It summarizes the completed Monday–Sunday calendar
week: pageviews, visitors, visits, and prior-week comparisons once coverage permits.
The first week discloses partial deployment-day coverage and verification visits.

Runtime: `~/.local/lib/thinx-tank-analytics/weekly-report.py`; standard Python,
no added packages. The report uses local Umami admin credentials and the existing
bridge token in place, never copied into Git or logs. It sends only to JD's DM
6996242753 through @thinxai_bot. No LAN access is required from thinx-muse.
Install the report script alongside backup.sh and its service/timer in the user
systemd directory; daemon-reload and enable/start the timer.

Use `python3 ops/analytics/weekly-report.py` to preview without sending.
`--test --send` delivers a labeled week-to-date test without consuming the weekly
report. A test was accepted by Telegram on September 21 (message ID 1857).
Five unit tests cover calendar weeks, DST, zero-baseline comparisons, coverage
labels and already-delivered suppression. Private delivery receipts live in
`~/.local/share/thinx-tank-analytics/reports/`. A file lock prevents overlapping
runs; a successful receipt suppresses repeat weekly sends. Network ambiguity
between delivery and receipt persistence can still cause a duplicate on retry.

Persistent scheduling catches up after downtime with the latest completed week;
it does not reconstruct every missed week. Failures retry at 15-minute intervals,
up to three starts per two hours, and remain visible in the service journal.
An API failure never becomes a false zero-traffic report. To disable delivery:
`systemctl --user disable --now analytics-weekly-report.timer`.

## GitHub weekly stats digest

Requested by JD on 2026-09-22 per thinx-muse's
`04-work-packages/WP-ANALYTICS-0001-umami/stats-digest-spec.md`.
`analytics-stats-digest.timer` runs Mondays at 06:00 America/Chicago,
independently of the existing 09:00 Telegram report. It publishes the previous
Monday–Sunday's totals, top ten pages/referrers, and seven daily pageview rows to
`ops/analytics/stats-weekly.md` on this repository's main branch.

Format version 1 has fixed metadata fields and four fixed section/table schemas.
Timestamps include their timezone offset. Counts are unformatted numbers.
Missing pre-deployment coverage is explicit. Umami 3.4 uses `type=path` instead
of the spec's obsolete `type=url`; daily values use seven stats queries with
Chicago calendar boundaries and inclusive end milliseconds. Daily pageviews must
reconcile to the whole-week total. Visitors are the weekly unique total, never
a sum of daily uniques.

Install stats-digest.py beside weekly-report.py in
`~/.local/lib/thinx-tank-analytics/`, and install the corresponding service/timer
in `~/.config/systemd/user/`. Enable with daemon-reload and
`systemctl --user enable --now analytics-stats-digest.timer`.
Preview: `python3 ops/analytics/stats-digest.py`.
Generate and publish now: `systemctl --user start analytics-stats-digest.service`.

The generator reads credentials locally, fetches and validates every response
before editing anything, then uses a fresh temporary main checkout to overwrite
only the digest. It commits with HCAE attribution, performs a normal fast-forward
push (never force), and verifies the remote SHA. Concurrent main changes cause a
safe failure and later fresh retry. A failed generation does not update the
previous digest or its timestamp; readers must check week and generated time.
The existing host GitHub credential helper provides authorized Git access.
Credentials and raw API responses are never written to the digest.

A lock prevents overlapping digest runs. The persistent timer catches up with
the latest completed week after downtime; up to three starts in two hours retry
failures at 15-minute intervals. Check `journalctl --user -u
analytics-stats-digest.service` and the timer's next-run timestamp for health.
The four digest tests cover stable tables/escaping, inconsistent daily totals,
API failure preventing publication, and top-ten validation/sorting.
