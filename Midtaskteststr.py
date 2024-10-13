#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_D, MoveDifferential, SpeedRPM
from ev3dev2.sensor import INPUT_4
from ev3dev2.wheel import EV3EducationSetTire
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sound import Sound

STUD_MM = 8
mdiff = MoveDifferential(OUTPUT_B,OUTPUT_D, EV3EducationSetTire, 119.25*STUD_MM) #was 11.75
Gyro = GyroSensor()
Gyro.reset()
Gyro.calibrate()
spkr = Sound()
distance_in = 84 #change this value
distance_mm = distance_in * 25.4

mdiff.odometry_start()
mdiff.on_to_coordinates(SpeedRPM(40),0,distance_mm) #x and y are in mm
mdiff.odometry_stop()
