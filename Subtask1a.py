#!/usr/bin/env python3
#import ev3 libs
from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveDifferential, SpeedRPM
from ev3dev2.sensor import INPUT_4
from ev3dev2.wheel import EV3EducationSetTire
from ev3dev2.sensor.lego import GyroSensor

STUD_MM = 8
mdiff = MoveDifferential(OUTPUT_A,OUTPUT_D, EV3EducationSetTire, 11.75*STUD_MM) #was 12.5
Gyro = GyroSensor(INPUT_4)
Gyro.reset()
Gyro.calibrate()
distance_cm = 120 #change the value
distance_mm = distance_cm*10
num_length = 5 #change the value
correction = 4

for lap in range(0,num_length):
    for correct in range(correction):
        mdiff.on_for_distance(SpeedRPM(20),distance_mm/correction)
        if Gyro.angle > 0:
            while Gyro.angle > .5 or Gyro.angle < -.5:
                mdiff.turn_left(SpeedRPM(15),.5)
        elif Gyro.angle < 0:
            while Gyro.angle > .5 or Gyro.angle < -.5:
                mdiff.turn_right(SpeedRPM(15),.5)
    distance_mm *= -1
    
#the x and y are in mm (10mm in 1 cm)