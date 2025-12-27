#!/bin/bash
set -e

LOG="/app/assets/server.log"
RULES="/app/assets/rules.txt"

ids=$(grep "^ERROR" "$LOG" \
  | grep -o "request_id=[0-9]\+" \
  | cut -d= -f2 \
  | sort -n \
  | uniq)

result=""

echo "IDs found:"
echo "$ids"
echo "--------------------"

for id in $ids; do
  val=$((id * 7))
  hex=$(printf "%x" "$val")

  echo "ID=$id  →  id*7=$val  →  hex=$hex"

  result+="$hex"
done

echo "--------------------"
echo "Final concatenated string = $result"

echo -n "$result" | sha256sum | awk '{print $1}' > /app/output.txt

echo "SHA written to /app/output.txt"
