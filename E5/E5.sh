#!/bin/bash
#Axel Manuel Perales Teofilo
echo 'Ingrese la API key:'
read -rs APIKEY

API-Request() {
while read i; do 
    printf "Correo: $i\n"
    curl -H "hibp-api-key:$APIKEY" -H "user-agent: Studies" -isS "https://haveibeenpwned.com/api/v2/breachedaccount/$i" > info.txt

    if grep -q "HTTP/2 404" info.txt; then
        echo "Tu cuenta no ha sido vulnerada."
    else 
        echo "Tu cuenta ha sido vulnerada en los siguientes servicios: "
        grep "Name" info.txt
    fi

    printf "\n";
done < info.txt
}

API-Request
rm info.txt
