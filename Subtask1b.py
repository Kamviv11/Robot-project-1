#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.wheel import *
from ev3dev2.sensor.lego import *
#the * imports everything within the lib

STUD_MM = 8
mdiff = MoveDifferential(OUTPUT_A,OUTPUT_D, EV3EducationSetTire, 11.75*STUD_MM)
Gyro = GyroSensor()
Gyro.reset()
Gyro.calibrate()
distance_cm = 120 #change the value
distance_mm = distance_cm*10
num_lap = 5 #change the value
angle = 180
angle1 = 0
correction = 4
for lap in range(num_lap*2):
    
    for times in range(correction):
        mdiff.on_for_distance(SpeedRPM(20),distance_mm/correction)
        if Gyro.angle > angle1:
            while Gyro.angle > (angle1+.25) or Gyro.angle < (angle1-.25):
                mdiff.turn_left(SpeedRPM(5),.5)
        elif Gyro.angle < angle1:
            while Gyro.angle > (angle1+.25) or Gyro.angle < (angle1-.25):
                mdiff.turn_right(SpeedRPM(5),.5)
    
    while Gyro.angle <= angle:
        mdiff.turn_right(SpeedRPM(10),10)
    if Gyro.angle > angle:
        while Gyro.angle >= (angle+.25) or Gyro.angle <= (angle-.25):
            mdiff.turn_left(SpeedRPM(5),.5)
    elif Gyro.angle < angle:
        while Gyro.angle >= (angle+.25) or Gyro.angle <= (angle-.25):
            mdiff.turn_right(SpeedRPM(5),.5)
    angle += 180
    angle1 += 180