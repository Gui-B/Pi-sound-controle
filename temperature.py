#!/usr/bin/python
import pyowm
import lcd
lcd16 = lcd.lcd(0x3f)
lcd20 = lcd.lcd(0x27)
while True:
    owm = pyowm.OWM('d1063f632e75759f0dedbcae4ab9e830')
    observation = owm.weather_at_place('Toulouse,fr')
    w = observation.get_weather()
    temp = w.get_temperature('celsius')

