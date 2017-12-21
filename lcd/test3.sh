#!/bin/bash

# récupération de la température ; on obtient ici une valeur à 5 chiffres sans virgules (ex: 44123) :
TEMP=$(cat /sys/class/thermal/thermal_zone0/temp)

# on divise alors la valeur obtenue par 1000, pour obtenir un résultat avec deux chiffres seulement (ex: 44) :
TEMP=$(($TEMP/1000))

DATE=`date +"%d-%m-%Y %H:%M:%S"`

python /root/rpi-lcd/scripts/repeater "$DATE" "$TEMP°C"
