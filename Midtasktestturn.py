#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.wheel import *
from ev3dev2.sensor.lego import *
from ev3dev2.sound import *

STUD_MM = 8
mdiff = MoveDifferential(OUTPUT_B,OUTPUT_D, EV3EducationSetTire, wheel_distance_mm=121.92) #was 11.75
tank = MoveTank(OUTPUT_B,OUTPUT_D)
tank.gyro = GyroSensor(INPUT_4)
tank.gyro.calibrate()
Gyro = GyroSensor(INPUT_4)
Gyro.reset()
Gyro.calibrate()
spkr = Sound()
distance_in = 96 #change this value for after the turn
distance_mm = distance_in * 25.4 
distance_y = 12*25.4
#mdiff.odometry_start()

#mdiff.on_to_coordinates(SpeedRPM(40),distance_mm,distance_y) x and y are in mm

#mdiff.odometry_stop()

mdiff.on_for_distance(SpeedRPM(20),distance_y,brake = True)
sleep(.5)
tank.turn_degrees(SpeedPercent(3),90,brake = True, sleep_time=.1)
while Gyro.angle != 90:
    if Gyro.angle > 90:
        mdiff.turn_left(SpeedRPM(15),.25)
    elif Gyro.angle < 90:
        mdiff.turn_right(SpeedRPM(15),.25)
sleep(2)
mdiff.on_for_distance(SpeedRPM(20),distance_mm,brake = True)
spkr.play_file("do-it-again.wav")
