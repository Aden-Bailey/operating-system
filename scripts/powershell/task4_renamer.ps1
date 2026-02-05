$files = Get-ChildItem -Filter "*.txt" -File

if ($files.Count -eq 0) {
  Write-Host "No .txt files found in current directory."
  exit 0
}

foreach ($f in $files) {
  if ($f.Name -like "OLD_*") {
    Write-Host "Skipping already-prefixed file: $($f.Name)"
    continue
  }

  $newName = "OLD_" + $f.Name
  $targetPath = Join-Path $f.DirectoryName $newName

  if (Test-Path $targetPath) {
    Write-Host "Cannot rename $($f.Name) -> $newName (target exists)"
    continue
  }

  Rename-Item -Path $f.FullName -NewName $newName
  Write-Host "Renamed: $($f.Name) -> $newName"
}