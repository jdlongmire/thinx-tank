# WP-ANALYTICS-0001 — Thinx-Tank analytics deployment

Status: deployed and verified; human acceptance pending. Repository: jdlongmire/thinx-tank.
Owner: thinx-003. Coordination record: jdlongmire/thinx-muse,
04-work-packages/WP-ANALYTICS-0001-umami.

Authority: JD granted end-to-end execution in the 2026-09-21 Console conversation
following the recommendation to host on thinx-003. This includes scoped runtime,
tunnel/DNS, private dashboard, blog integration, publication and verification.
It supersedes the earlier manual-deployment handoff; no unrelated services change.

Acceptance checks:
- Systemd manages isolated, resource-limited Umami and PostgreSQL containers.
- Public HTTPS serves the tracker and accepts pageviews; dashboard and admin APIs
  return 404 through that public hostname (live positive and negative HTTP checks).
- Dashboard is reachable via tailnet HTTPS, with a non-default admin credential.
- Deployed Hugo pages include the tracker; a real browser visit produces a pageview
  visible through the authenticated analytics API.
- A scheduled database backup runs, and a restore into a separate temporary database
  reproduces the website/event data.
- Runtime configuration, operating instructions and evidence are committed and
  published. Secrets remain outside Git. Verification is not human acceptance.

Human-Curated, AI-Enabled (HCAE)
