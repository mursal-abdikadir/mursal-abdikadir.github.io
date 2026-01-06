# wifi-reset.ps1
# Resets Wi-Fi adapter — handy when "No Internet" strikes
# Usage: Run as Admin in PowerShell

$adapter = Get-NetAdapter | Where-Object {$_.Name -like "*Wi-Fi*" -or $_.Name -like "*Wireless*"}

if ($adapter) {
    Write-Host "Resetting Wi-Fi adapter: $($adapter.Name)" -ForegroundColor Green
    Restart-NetAdapter -Name $adapter.Name
    Write-Host "Done. Try reconnecting in 10 seconds." -ForegroundColor Cyan
} else {
    Write-Host "No Wi-Fi adapter found. Check hardware or try Ethernet." -ForegroundColor Red
}
