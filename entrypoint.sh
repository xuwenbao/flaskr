#!/usr/bin/env bash
set -e

if [ ! -f "flaskr.db" ]; then
    python -m flask initdb
fi

echo "Starting server($@), Please wait ...."
exec "$@"