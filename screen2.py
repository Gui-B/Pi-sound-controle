#!/usr/bin/python
import lcd
import os
from time import sleep
lcd20 = lcd.lcd(0x27)
line1 = ""
line2 = ""
line3 = ""
line4 = ""
light = None
while True:
    if True if os.system("ping -c 1 10.42.1.100 > /dev/null") is 0 else False:
        if not light or light is None:
            lcd20.backlight(1)
            light = True
        file = open("/gpio/nom", "r")
        name = file.read()
        file.close
        source = "Source : " + name
        if line1 != source:
            lcd20.printlcd(source + "          ", 1)
            line1 = source
    else:
        if light or light is None:
            lcd20.backlight(0)
            light = False
    sleep(0.1)
