#!/bin/bash
set -euo pipefail
umask 077
backup_dir="$HOME/.local/share/thinx-tank-analytics/backups"
mkdir -p "$backup_dir"
backup_file="$backup_dir/umami-$(date -u +%Y%m%dT%H%M%SZ).dump"
podman exec thinx-tank-analytics-db pg_dump -U umami -d umami -Fc > "$backup_file.tmp"
test -s "$backup_file.tmp"
mv "$backup_file.tmp" "$backup_file"
sha256sum "$backup_file" > "$backup_file.sha256"
find "$backup_dir" -maxdepth 1 -type f -name 'umami-*.dump*' -mtime +30 -delete
printf 'Database backup completed: %s\n' "$backup_file"
