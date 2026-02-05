Write-Host "Top 5 processes by memory usage:"
Get-Process |
  Sort-Object WorkingSet64 -Descending |
  Select-Object -First 5 @{Name="Name";Expression={$_.ProcessName}},
                      @{Name="PID";Expression={$_.Id}},
                      @{Name="MemoryMB";Expression={[math]::Round($_.WorkingSet64/1MB,2)}} |
  Format-Table -AutoSize