#!/usr/bin/python
from pcf8574 import PCF8574
from time import sleep
import soundRelay as rl
import lcd

i2c_port_num = 1
btn_add = 0x38

btn = PCF8574(i2c_port_num, btn_add)
s = rl.soundrelay()

while True:
    if btn.port[0] is False:
        s.set(3)
    elif btn.port[1] is False:
        s.set(2)
    elif btn.port[2] is False:
        s.set(4)
    elif btn.port[3] is False:
        s.set(1)
    elif btn.port[4] is False:
        s.set(5)
    elif btn.port[5] is False:
        lcd16 = lcd.lcd(0x3f)
        #lcd20 = lcd.lcd(0x27)
        lcd16.backlight(0)
        #lcd20.backlight(0)
    sleep(0.1)

