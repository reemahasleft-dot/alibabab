$Source = "E:\Sovereign_Archives"
$HashFile = "D:\Sovereign_System\Integrity_Manifest.txt"

Write-Host ">>> SCANNING SECTORS FOR INTEGRITY..." -ForegroundColor Yellow
Get-ChildItem -Path $Source -Recurse -File | ForEach-Object {
    $Hash = Get-FileHash -Path $_.FullName -Algorithm MD5
    "$($Hash.Hash) | $($_.FullName) | $($_.LastWriteTime)" | Out-File -FilePath $HashFile -Append
}
Write-Host ">>> INTEGRITY MANIFEST UPDATED. DATA IS SECURED." -ForegroundColor Green
