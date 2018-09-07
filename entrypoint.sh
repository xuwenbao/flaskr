#!/usr/bin/env sh
set -e

if [ ! -f "flaskr.init" ]; then
    python -m flask initdb
    touch flaskr.init
fi

echo "Starting server($@), Please wait ...."
exec "$@"
