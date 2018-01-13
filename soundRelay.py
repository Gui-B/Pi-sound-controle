#!/usr/bin/python
from pcf8574 import PCF8574
import lcd

class soundrelay:

    i2c_port_num = 1
    pcf_address = 0x20
    pcf = None
    lcd16 = None

    def __init__(self):
        self.pcf = PCF8574(self.i2c_port_num, self.pcf_address)
        #lcd16 = lcd.lcd(0x3f)

    def clear(self):
        self.pcf.port[3] = True
        self.pcf.port[4] = True
        self.pcf.port[5] = True
        self.pcf.port[6] = True
        self.pcf.port[7] = True

    def write(self, num, name):
        file = open("/gpio/id", "w")
        file.write(str(num))
        file.close()
        file = open("/gpio/nom", "w")
        file.write(name)
        file.close

    def read(self):
        file = open("/gpio/id", "r")
        id = file.read()
        file.close()
        id = int(id)
        return id

    def set(self, num):
        oldnum = self.read()
        if oldnum != num:
            lcd16 = lcd.lcd(0x3f)
            #lcd20 = lcd.lcd(0x27)
            lcd16.backlight(1)
            #lcd20.backlight(1)
            self.clear()
            name = ""
            if num == 1:
                name = "Salon"
                self.pcf.port[3] = False
            elif num == 2:
                name ="Kriss"
                self.pcf.port[4] = False
            elif num == 3:
                name = "FreeBox"
                self.pcf.port[5] = False
            elif num == 4:
                name = "TV"
                self.pcf.port[6] = False
            elif num == 5:
                name = "Cyke"
                self.pcf.port[7] = False
            self.write(num, name)
            lcd16.printlcd("Source : " + name, 1)
            #lcd20.printlcd("Source : " + name, 1)
        else:
            lcd16 = lcd.lcd(0x3f)
            #lcd20 = lcd.lcd(0x27)
            lcd16.backlight(1)
            #lcd20.backlight(1)
            name = ""
            if num == 1:
                name = "Salon"
            elif num == 2:
                name ="Kriss"
            elif num == 3:
                name = "FreeBox"
            elif num == 4:
                name = "TV"
            elif num == 5:
                name = "Cyke"
            lcd16.printlcd("Source : " + name, 1)
            #lcd20.printlcd("Source : " + name, 1)
        #lcd16.printlcd(name, 2)




