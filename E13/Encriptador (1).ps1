param([string]$file)

$FileContent = Get-Content $file
$FileContentBytes = [System.Text.Encoding]::UTF8.GetBytes($FileContent)
$FileContentEncoded = [System.Convert]::ToBase64String($FileContentBytes)

$FileContentEncoded | Set-content ($file + ".b64")

Write-Host "[+]File"$file" Encoded Sucessfully"
