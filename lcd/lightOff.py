#!/usr/bin/python
#
# repeater
#
# Accepts up to 2 arguments and dumps the contents out
# to the 2 lines on the attached LCD screen. This file
# is referenced by the various scripts in this repo.
#
# Usage: python repeater stringLine1 stringLine2
#
##

import sys
import lcd1602
import lcd2004
from time import *

lcd1602 = lcd1602.lcd()
lcd2004 = lcd2004.lcd()

lcd1602.backlight(0)
lcd2004.backlight(0)

sleep(0.005)

