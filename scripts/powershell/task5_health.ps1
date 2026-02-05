Write-Host "===== System Health Snapshot ====="
Write-Host ("Date/Time : {0}" -f (Get-Date))
Write-Host ("Hostname  : {0}" -f $env:COMPUTERNAME)
Write-Host ("User      : {0}" -f $env:USERNAME)
Write-Host ""

$drive = Get-PSDrive -Name C
$totalGB = [math]::Round(($drive.Used + $drive.Free) / 1GB, 2)
$freeGB  = [math]::Round($drive.Free / 1GB, 2)

Write-Host "Disk Usage (C:)"
Write-Host ("Free:  {0} GB" -f $freeGB)
Write-Host ("Total: {0} GB" -f $totalGB)
Write-Host "=================================="