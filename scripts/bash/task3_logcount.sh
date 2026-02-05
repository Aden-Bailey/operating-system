#!/usr/bin/env bash

# Create dummy log file
cat > server.log << 'EOF'
INFO Server started
INFO Listening on port 8080
ERROR Database connection failed
INFO Retrying connection
ERROR Authentication Error for user admin
WARN Low disk space
INFO Request handled
ERROR Timeout Error while reading
EOF

# Count lines containing "Error" (case-sensitive match as requested)
COUNT=$(grep -c "Error" server.log)

echo "server.log created."
echo "Lines containing 'Error': $COUNT"