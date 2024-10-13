#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.wheel import EV3EducationSetTire
from ev3dev2.sensor.lego import *
from ev3dev2.sound import *

tank = MoveTank(OUTPUT_B, OUTPUT_D)
ulra = UltrasonicSensor(INPUT_2)
color_left = ColorSensor(INPUT_1)
color_right = ColorSensor(INPUT_4)
med = MediumMotor(OUTPUT_C)
# Initialize the tank's gyro sensor
tank.gyro = GyroSensor()

# Calibrate the gyro to eliminate drift, and to initialize the current angle as 0
tank.gyro.calibrate()
Gyro = GyroSensor(INPUT_3)
Gyro.reset()
Gyro.calibrate()

med.on_for_rotations(SpeedPercent(20),-2)
    # Follow the target_angle for 4500ms
