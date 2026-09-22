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

## Weekly report addition — 2026-09-21

Authority: JD requested a weekly statistics report to his Telegram DM.
Implemented a Python reporter and persistent user-systemd timer for Mondays
09:00 America/Chicago. Next scheduled send: 2026-09-28 09:00 CDT.
Five unit tests pass, including DST and duplicate suppression. A labeled
week-to-date test (4 pageviews / 1 visitor / 1 visit, with setup-traffic caveat)
was accepted by Telegram for the configured DM, message ID 1857.
The production timer is enabled; no ordinary weekly report was sent early.

## GitHub digest addition — 2026-09-22

Authority: JD explicitly requested Monday approximately 06:00 America/Chicago
generation and main-branch publication per thinx-muse's stats-digest-spec.md.
Four digest tests and all five existing Telegram report tests pass. The
installed Umami API rejects type=url with 400; type=path is verified against
Umami 3.4 source and live nonempty results. Daily totals are checked against
weekly pageviews. The initial completed-week artifact covers September 14–20
and explicitly identifies pre-tracking lack of coverage. The first scheduled
run is September 28 at 06:00 CDT; Telegram remains at 09:00 CDT.
