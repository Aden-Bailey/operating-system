@"
INFO Server started
INFO Listening on port 8080
ERROR Database connection failed
INFO Retrying connection
ERROR Authentication Error for user admin
WARN Low disk space
INFO Request handled
ERROR Timeout Error while reading
"@ | Set-Content -Path "server.log"

# Count lines containing "Error" (case-sensitive)
$Count = (Select-String -Path "server.log" -Pattern "Error" -CaseSensitive).Count

Write-Host "server.log created."
Write-Host "Lines containing 'Error': $Count"