#!/usr/bin/env bash

echo "Top 5 processes by memory usage:"
echo "NAME                          PID     %MEM"
ps -eo comm,pid,%mem --sort=-%mem | head -n 6 | awk 'NR==1{next} {printf "%-28s %-7s %s\n",$1,$2,$3}'