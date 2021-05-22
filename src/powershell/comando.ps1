<#
    Autor: Andrés Hernández Mata
    Fecha: 21/05/2021
    Version: 1.0.0
#>

param(    
    [string]$comando    
)

try {

    Write-Host "Windows PowerShell"
    Invoke-Expression $comando

} catch {
    Write-Host $(Get-Date) " [ERROR] Ha ocurrido un error"
    $_.Exception.Message
}