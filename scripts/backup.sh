#!/bin/sh -e

if [ $# -ne 4 ]; then
    echo "Usage: $0 <PGHOST> <PGPORT> <PGUSER> <PGDB>"
    exit 1
fi

PGHOST="$1"
PGPORT="$2"
PGUSER="$3"
PGDB="$4"

echo "Backup process started."

# Save the current date in YYYY-MM-DD format to a variable
current_datetime=$(date +%Y-%m-%d-%H%M%S)

backup_directory="./backups"
backup_filename="${backup_directory}/backup-${current_datetime}.dump.gz"

# Ensure the backup directory exists
mkdir -p "$backup_directory"

# Run pg_dump and compress its output, then save to /backups with the current date in the filename
pg_dump -Fc "$PGDB" -U "$PGUSER" -h "$PGHOST" -p "$PGPORT" | gzip >"$backup_filename"

echo "Backup has been created and saved to ${backup_filename}"
