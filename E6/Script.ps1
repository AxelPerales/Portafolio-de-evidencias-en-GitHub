#Axel Manuel Perales Teofilo
import-module ModulosTareas
do{
    menu
    $input = Read-Host "Selecciona opción: "
    switch($input)
    {
        '1' { #función Ver-StatusPerfil
        'Opción #1'
        Ver-StatusPerfil
        }
        '2' { #función Cambiar-StatusPerfil
        'Opción #2'
        Cambiar-StatusPerfil
        }
        '3' { #función Ver-PerfilRedctual
        'Opción #3'
        Ver-PerfilRedActual
        }
        '4' { #salir
        return
        }
    } 
    Pause
}
until(input -eq '4')
