$SourceDir = "E:\Sovereign_Archives\Source_Code"
$DestDir = "E:\Sovereign_Archives\System_Snapshots"
$Timestamp = Get-Date -Format "yyyy-MM-dd_HHmm"
$ZipName = "$DestDir\Snapshot_$Timestamp.zip"

Write-Host ">>> CAPTURING SYSTEM STATE..." -ForegroundColor Yellow
if (Test-Path $SourceDir) {
    Compress-Archive -Path "$SourceDir\*" -DestinationPath $ZipName -CompressionLevel Optimal
    Write-Host ">>> SNAPSHOT SECURED: $ZipName" -ForegroundColor Green
}
