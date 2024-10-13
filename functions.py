#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.wheel import *
from ev3dev2.sensor.lego import *
from ev3dev2.sound import *
from ev3dev2.sound import *

spkr = Sound()
mdiff = MoveDifferential(OUTPUT_B,OUTPUT_D, EV3EducationSetTire, wheel_distance_mm=121.92)
distance_in = .5 #change this value
distance_mm = distance_in * 25.4
inchs = 25.4
tank = MoveTank(OUTPUT_B,OUTPUT_D)
medium = MediumMotor(OUTPUT_C)
Gyro = GyroSensor(INPUT_3)
Gyro.reset()
Gyro.calibrate()
#allows the tank to know that gyro is working with it
tank.gyro = GyroSensor(INPUT_3)
tank.gyro.reset()
tank.gyro.calibrate()
ultra = UltrasonicSensor(INPUT_2)
color_left = ColorSensor(INPUT_1)
color_right = ColorSensor(INPUT_4)
medium = MediumMotor()


column_box = 1
row_box = 1
Shelf = ""
Shelf_num = 0
Location = 0
Barcode = []
Drop = ""
side = ""
def location_box(shelf,shelf_num, location, barcode, drop):
    
    global column_box
    global row_box
    global Shelf
    global Shelf_num
    global Location
    global Barcode
    global Drop
    global side
    
    if location > 6:
        side = "right"
    else:
        side = "left"
    Shelf = shelf
    Shelf_num = shelf_num
    Location = location % 6
    Barcode = barcode
    Drop = drop
    if shelf == "B" or shelf == "D":
        column_box = 2
    if shelf == "A" or shelf == "B":
        if shelf_num == 1:
            if location >= 7:
                row_box = 2
        else:
            if location < 7:
                row_box = 2
            else:
                row_box = 3
    else:
        row_box += 1
        if shelf_num == 1:
            if location >= 7:
                row_box = 4
        else:
            if location < 7:
                row_box = 4
            else:
                row_box = 5
def correction(targetangle):
    x = targetangle - tank.gyro.angle
    tank.turn_degrees(
        speed = SpeedPercent(10),
        target_angle=x,
        brake = True,
        sleep_time = .1
    )
def move_straight(inch,angle,correct):
    for x in range(correct + 1):
        tank.follow_gyro_angle(
            kp = 11.3, ki = .05, kd = 3.2,
            speed = SpeedPercent(15),
            target_angle=angle,
            follow_for=follow_for_ms,
            ms = (inch * 335) / (correct + 1)
        )
        correction(angle)
def move_backwards(inch,angle,correct):
    for x in range(correct + 1):
        tank.follow_gyro_angle(
            kp = 11.3, ki = .05, kd = 3.2,
            speed = SpeedPercent(-15),
            target_angle=angle,
            follow_for=follow_for_ms,
            ms = (inch * 335) / (correct + 1)
        )
        correction(angle)
def move_turn(angle):
    tank.turn_degrees(
        speed = SpeedPercent(5),
        target_angle=angle,
        brake = True,
        sleep_time = .1
    )
def nav_box():
    move_straight(12 + 24*(row_box-2),0,row_box)
    move_turn(90)
    if column_box == 2:
        move_straight(48,90,2)
        if Location == 0:
            move_straight(39,90,2)
        else:
            move_straight(9+6*(Location-1),90,1)
    else:
        if Location == 0:
            move_straight(39,90,2)
        else:
            move_straight(9+6*(Location-1),90,1)
def pick_up():
    if side == "left":
        move_turn(-90)
    else:
        move_turn(90)
def nav_backhome():
    if Drop == "C":
        move_backwards(120,0,4)
    elif Drop == "B":
        move_backwards(12,180,1)
        move_turn(-90)
        move_backwards(96,90,3)
        move_turn(-90)
        move_backwards(12,0,1)
    elif Drop == "D":
        move_backwards(108,0,4)
        move_turn(90)
        move_backwards(96,90,3)
        move_turn(-90)
        move_backwards(12,0,1)
def scan():
    x = 0
    array = []
    if side == "right":
        move_turn(90)
        correction(180)
        if ultra.distance_centimeters > 2.2:
            x = (ultra.distance_centimeters - 2.2) * 0.393701
            move_straight(x,180,0)
        move_turn(-90)
        move_straight(2.2,90,0)
        sleep(2)
        while color_right.reflected_light_intensity < 8 and color_right.reflected_light_intensity > 1:
            mdiff.on_for_distance(SpeedPercent(10),-5)
        
        sleep(2)
        for x in range(4):
            if color_right.reflected_light_intensity <= 8 and color_right.reflected_light_intensity >= 1:
                array.append(1)
            else:
                array.append(0)
            mdiff.on_for_distance(SpeedPercent(10),-25.4*.5)
            sleep(2)
        if array != Barcode:
            spkr.beep()
        else:
            spkr.beep()
            spkr.beep()
            spkr.beep()
        move_straight(.4375,90,0)
        move_turn(90)
        move_backwards(x,180,0)
        move_turn(-90)
    else:
        move_turn(-90)
        if ultra.distance_centimeters > 2.2:
            x = (ultra.distance_centimeters - 2.2) * 0.393701
            move_straight(x,0,0)
        move_turn(90)
        while color_left.reflected_light_intensity != 0:
             move_backwards(.2,90,0)
        
        sleep(2)
        while color_left.reflected_light_intensity < 8 and color_left.reflected_light_intensity > 1:
            mdiff.on_for_distance(SpeedPercent(10),5)
        
        sleep(2)
        for x in range(4):
            if color_left.reflected_light_intensity <= 8 and color_left.reflected_light_intensity >= 1:
                array.append(1)
            else:
                array.append(0)
            mdiff.on_for_distance(SpeedPercent(10),25.4*.5)
            sleep(2)
        if array != Barcode:
            spkr.beep()
        else:
            spkr.beep()
            spkr.beep()
            spkr.beep()
        move_straight(.4375,90,0)
        move_turn(-90)
        move_backwards(x,0,0)
        move_turn(90)

def Subtask1():
    nav_box()
    sleep(5)
    if column_box == 2:
        if Location == 0:
            move_straight(9,90,0)
        else:
            move_straight(90-48-1-6*(Location-1),90,2)
    else:
        if Location == 0:
            move_straight(57,90,2)
        else:
            move_straight(90-3-6*(Location-1),90,4)
    move_turn(90)
    move_straight(12+24*(row_box-1),180,2)
def Subtask2():
    move_backwards(12,0,0)
    move_turn(-90)
    move_backwards(96,-90,4)
    move_turn(-90)
    move_backwards(12,-180,0)
def Subtask3():
    move_turn(90)
    move_straight(21,90,2)
    scan()
    move_turn(90)
    medium.on_for_rotations(SpeedPercent(20),4)
    move_straight(3,180,0)
    medium.on_for_rotations(SpeedPercent(20),-2)
    move_backwards(3,180,0)
    move_turn(-90)
    move_straight(26,90,2) #change to 21 if need be  
def SUBSubtask3():
    move_turn(90)
    move_straight(21,90,2)
    scan()
    move_straight(26,90,2)


location_box("C",2,5,[1,0,1,0],"C")
nav_box()
scan()
if side == "right":
    move_turn(90)
    medium.on_for_rotations(SpeedPercent(20),4)
    move_straight(3,180,0)
    medium.on_for_rotations(SpeedPercent(20),-2)
    move_backwards(3,180,0)
    move_turn(-90)
else:
    move_turn(-90)
    medium.on_for_rotations(SpeedPercent(20),4)
    move_straight(3,0,0)
    medium.on_for_rotations(SpeedPercent(20),-2)
    move_backwards(3,0,0)
    move_turn(90)
if Drop == "B":
    if column_box == 2:
        if Location == 0:
            move_straight(9,90,0)
        else:
            move_straight(90-48-1-6*(Location-1),90,2)
    else:
        if Location == 0:
            move_straight(57,90,2)
        else:
            move_straight(90-3-6*(Location-1),90,4)
    move_turn(90)
    move_straight(12+24*(row_box-1),180,2)
elif Drop == "C":
    if column_box == 2:
        if Location == 0:
            move_backwards(39,90,2)
            move_backwards(48,90,2)
        else:
            move_backwards(9+6*(Location-1),90,1)
    else:
        if Location == 0:
            move_backwards(39,90,2)
        else:
            move_backwards(9+6*(Location-1),90,1)
    move_turn(-90)
    move_straight(108-24*(row_box-1),0,4)
medium.on_for_rotations(SpeedPercent(20),2)
nav_backhome()


#nav code will contain nav to box and obsaticale avoid