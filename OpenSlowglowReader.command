#!/bin/zsh
set -e
cd "$(dirname "$0")"

port=8787
while lsof -iTCP:$port -sTCP:LISTEN >/dev/null 2>&1; do
  port=$((port + 1))
done

python3 -m http.server "$port" >/tmp/slowglow-reader.log 2>&1 &
server_pid=$!

sleep 0.8
open "http://127.0.0.1:$port/"

echo "慢光阅读 Slowglow Reader is running at http://127.0.0.1:$port/"
echo "Close this window to stop the local server."
wait "$server_pid"
