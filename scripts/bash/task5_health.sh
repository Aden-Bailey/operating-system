#!/usr/bin/env bash

echo "===== System Health Snapshot ====="
echo "Date/Time : $(date)"
echo "Hostname  : $(hostname)"
echo "User      : $(whoami)"
echo

# Root filesystem usage (human readable)
echo "Disk Usage (/):"
df -h / | awk 'NR==1{print $0} NR==2{print $0}'
echo "=================================="