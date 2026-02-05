#!/usr/bin/env bash
# Usage: ./task1_bigfile.sh <filename>

if [ $# -ne 1 ]; then
  echo "Usage: $0 <filename>"
  exit 1
fi

FILE="$1"
LIMIT=1048576

if [ ! -e "$FILE" ]; then
  echo "Error: File does not exist: $FILE"
  exit 1
fi

# Get size in bytes (portable-ish)
SIZE=$(wc -c < "$FILE")

echo "File: $FILE"
echo "Size: $SIZE bytes"

if [ "$SIZE" -gt "$LIMIT" ]; then
  echo "Warning: File is too large"
else
  echo "File size is within limits."
fi