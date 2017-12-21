import lcddriver
from time import *

lcd = lcddriver.lcd()

# lcd.lcd_clear();
lcd.lcd_display_string("Lorem", 1)
lcd.lcd_display_string("Ipsum", 2)

sleep(2)

lcd.lcd_write(0x00)
