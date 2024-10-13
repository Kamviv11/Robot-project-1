#!/usr/bin/env python3
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import *
col = ColorSensor()
col.MODE_COL_REFLECT = 'COL-REFLECT'
x = True
while x == True:
    print(col.reflected_light_intensity)