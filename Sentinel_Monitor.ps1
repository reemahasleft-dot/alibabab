while ($true) {
    $Temp = (Get-WmiObject -Namespace root\wmi -Class MsAcpi_ThermalZoneTemperature).CurrentTemperature
    $TempCelsius = ($Temp / 10) - 273.15
    $Timestamp = Get-Date -Format "HH:mm:ss"
    
    if ($TempCelsius -gt 90) {
        Write-Host "[$Timestamp] WARNING: CRITICAL TEMP DETECTED: $TempCelsius C" -ForegroundColor Red
    } else {
        Write-Host "[$Timestamp] SENTINEL STABLE: $TempCelsius C" -ForegroundColor Green
    }
    Start-Sleep -Seconds 10
}
