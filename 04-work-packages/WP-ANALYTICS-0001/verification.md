# Verification evidence

Verified 2026-09-21 on thinx-003. Human-Curated, AI-Enabled (HCAE).

Deployment commit: 3852ad6591657721c5a491c013f5fa1ee3de94a2.
GitHub Pages run: https://github.com/jdlongmire/thinx-tank/actions/runs/35643404346
Result: success.

- Hugo 0.166.0 production build passed. HTML-parser validation found exactly one
  correctly configured tracker in all 16 generated HTML documents. Existing
  languageCode deprecation warnings remain unrelated to this change.
- Cloudflare ingress validator passed. Public script returned 200; public root
  and /api/websites returned 404. Public traffic reaches only script.js/api/send.
- Rootless app/database, tunnel and backup timer are active. Systemd reports
  app MemoryMax 1610612736 / CPU quota 150%; DB 805306368 / CPU quota 100%.
- The real-browser verifier (`ops/analytics/verify-browser.py`, Playwright using
  system Chromium) loaded the deployed blog, observed script.js=200 and
  api/send=200, logged in through the tailnet dashboard and found Thinx-Tank.
- Authenticated stats API reported 4 pageviews, 1 visitor, 1 visit at final
  verification. These initial events include verification traffic. The first
  default headless-browser user agent was filtered and created no event;
  a normal browser user agent passed. A 200 ingestion response alone therefore
  was not treated as proof of storage.
- A separate Do Not Track browser context emitted no collection request.
- The app service was restarted and subsequently passed browser/API checks;
  persisted website and event data survived. Host reboot was not performed.
- Manual invocation of the daily backup service created a checksum-validated
  custom PostgreSQL dump. pg_restore --exit-on-error restored it into the
  separate analytics_restore_verify database. Both databases had 1 website
  and 1 event at that snapshot. Later browser checks added further live events.
- The default admin password was replaced before browser dashboard access.
  Public sharing is disabled and recording/replay is disabled.

Limits: backups are local, with 30-day retention; no off-host copy is configured.
Host/network downtime causes collection gaps while the GitHub Pages blog stays
available. Tailscale dashboard access was tested from this host, not JD's device.
Verification is not a declaration of Principal Operator acceptance.
