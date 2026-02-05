param(
  [Parameter(Mandatory=$true)]
  [string]$File
)

$Limit = 1048576

if (-not (Test-Path $File)) {
  Write-Host "Error: File does not exist: $File"
  exit 1
}

$Size = (Get-Item $File).Length
Write-Host "File: $File"
Write-Host "Size: $Size bytes"

if ($Size -gt $Limit) {
  Write-Host "Warning: File is too large"
} else {
  Write-Host "File size is within limits."
}