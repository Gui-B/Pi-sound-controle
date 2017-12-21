#!/usr/bin/python
import sys
sys.path.append("/root/rpi-lcd")
import lcd

class lcd16x2:
    address = 0x3f
    sc = None

    def __init__(self):
        self.sc = lcd.lcd(address)

    def lightOn(self):
        self.sc.backlight(1)

    def lightOff(self):
        self.sc.backlight(0)

    def write(self, txt, line):
        self.sc.printlcd(txt, line)

