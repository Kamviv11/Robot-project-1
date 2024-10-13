#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.wheel import *
from ev3dev2.sensor.lego import *
from ev3dev2.sound import *

tank = MoveTank(OUTPUT_B,OUTPUT_D)
#allows the tank to know that gyro is working with it
tank.gyro = GyroSensor(INPUT_4)
tank.gyro.calibrate()
#wait for 2 seconds
sleep(2)

tank.turn_degrees(
    speed = SpeedPercent(5),
    target_angle=180,
    brake = True,
    sleep_time = .1
)
tank.off()
exit()

#holding ctrl on the function shows where the function is from