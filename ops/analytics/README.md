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
