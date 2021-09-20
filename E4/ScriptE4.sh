#!/bin/bash
function s_o {
  if type -t wevtutil &> /dev/null
  then
     OS=MSWin
  elif type -t scutil &> /dev/null 
  then
     OS=macOS
  else
     OS=Linux
  fi
  echo "Tú sistema operativo es: $OS">>IPS.txt
}
echo "Ejecución..."
s_o
function live_ping { 
     ping -c 1 $1 > /dev/null 2>&1
     [ $? -eq 0 ] && echo "IP: $ip up." >> IPS.txt
}
for ip in 192.168.0.{1..255}
do 
live_ping $ip & disown
host=$ip
first=10
last=500
function portscan {
for ((counter=$first; counter<=$last; counter++))
do
    (echo> /dev/tcp/$host/$counter) > /dev/null 2<&1 && echo "Puerto: $counter open" >> IPS.txt
done
}
portscan
done
echo "Ejecución exitosa"
