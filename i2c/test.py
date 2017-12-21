#!/usr/bin/python

import sys
sys.path.append("/root/rpi-lcd")
import lcd
import time


lcd1 = lcd.lcd(0x27)
lcd2 = lcd.lcd(0x3f)
lcd1.backlight(1)
lcd2.backlight(1)
lcd1.printlcd( "blbl", 1)
time.sleep(1)
lcd1.printlcd( "blbl", 2)
time.sleep(1)
lcd1.printlcd("blbl", 3)
time.sleep(1)
lcd1.printlcd("blbl", 4)
time.sleep(2)
lcd2.printlcd("blbl", 1)
time.sleep(1)
lcd2.printlcd("blbl", 2)
time.sleep(2)
lcd1.backlight(0)
lcd2.backlight(0)
