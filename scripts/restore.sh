#!/bin/sh -e

# The directory where backups are stored
BACKUP_DIRECTORY="./backups"

if [ $# -lt 5 ]; then
    echo "Usage: $0 <BACKUP_FILE> <PGHOST> <PGPORT> <PGUSER> <PGDB>"
    exit 1
fi

file_name="$1"
PGHOST="$2"
PGPORT="$3"
PGUSER="$4"
PGDB="$5"

# Full path to the file
full_file_path="${BACKUP_DIRECTORY}/${file_name}"

# Check if the file exists
if [ ! -f "$full_file_path" ]; then
    echo "File ${file_name} does not exist."
    exit 1
fi

if psql -h "$PGHOST" -U "$PGUSER" -p "$PGPORT" -lqt | cut -d \| -f 1 | grep -qw "$PGDB"; then
    # Terminate active sessions using the database
    echo "Terminating active connections to '$PGDB'..."
    psql -h "$PGHOST" -U "$PGUSER" -p "$PGPORT" -d "$PGDB" -c "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = '$PGDB' AND pid <> pg_backend_pid();"

    # Drop the database
    dropdb -h "$PGHOST" -U "$PGUSER" -p "$PGPORT" "$PGDB"
    echo "Database '$PGDB' dropped successfully."
else
    echo "Database '$PGDB' does not exist, skipping drop step."
fi

createdb -h "$PGHOST" -U "$PGUSER" -p "$PGPORT" --owner="$PGUSER" "$PGDB"

gunzip -c "$full_file_path" | pg_restore -h "$PGHOST" -U "$PGUSER" -p "$PGPORT" -d "$PGDB"

echo "Backup applied successfully."
