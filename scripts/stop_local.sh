#!/usr/bin/env bash
# Stop all local background services started by deploy.sh --local.
set -euo pipefail

stopped=0
for pidfile in /tmp/a2i2-*.pid; do
    [ -f "$pidfile" ] || continue
    name=$(basename "$pidfile" .pid | sed 's/a2i2-//')
    pid=$(cat "$pidfile")
    if kill "$pid" 2>/dev/null; then
        echo "  stopped $name (pid=$pid)"
        (( stopped++ ))
    else
        echo "  $name already gone (pid=$pid)"
    fi
    rm -f "$pidfile"
done

if [ "$stopped" -eq 0 ]; then
    echo "No local services running."
fi
