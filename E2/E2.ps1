#Axel Manuel Perales Teofilo
Ver-StatusPerfil
function Ver-StatusPerfil {
    param {[parameter(Mandatory)]
    [ValidateSet("Public", "Private")]
    [string] $perfil
    $status = Get-
    NotFirewallProfile -Name $perfil
    Write-Host "Perfil" $perfil
    if($status.enabled){
        Write-Host "Status: Activado"
    } else{
        Write-Host "Status: Desactivado"
    }
}
Cambiar-StatusPerfil
function Cambiar-StatusPerfil {
    param {[parameter(Mandatory)]
    [ValidateSet("Public", "Private")]
    [string] $perfil
    $status = Get-
    NotFirewallProfile -Name $perfil
    Write-Host "Perfil" $perfil
    if($status.enabled){
        Write-Host "Status: Activado"
        $opc = Read-Host -promt
        "¿Deseas desactivarlo? [Y] si [N] no"
        if ($opc -eq "Y"){
            Set-NetFirewallProfile -Name $perfil -Enabled False
        }
    } else{
        Write-Host "Status: Desactivado"
        $opc = Read-Host -promt
        "¿Deseas activarlo? [Y] si [N] no"
        if ($opc -eq "Y"){
            Set-NetFirewallProfile -Name $perfil -Enabled True
        }
    }
    Ver-StatusPerfil -perfil $perfil
}
Ver-PerfilRedActual
function Ver-PerfilRedActual{
    $perfilRed = Get-
    NetConnectionProfile
    Write-Host "Nombre de red: "
    $perfilRed.name
    Write-Host "Perfil de red: "
    $perfilRed.NetworkCategory
}
