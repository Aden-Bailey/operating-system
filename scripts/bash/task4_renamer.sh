#!/usr/bin/env bash

shopt -s nullglob

FILES=( *.txt )
if [ ${#FILES[@]} -eq 0 ]; then
  echo "No .txt files found in current directory."
  exit 0
fi

for f in "${FILES[@]}"; do
  if [[ "$f" == OLD_* ]]; then
    echo "Skipping already-prefixed file: $f"
    continue
  fi

  new="OLD_$f"
  if [ -e "$new" ]; then
    echo "Cannot rename $f -> $new (target exists)"
    continue
  fi

  mv -- "$f" "$new"
  echo "Renamed: $f -> $new"
done