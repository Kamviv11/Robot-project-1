IsStraight = bool(input("Is the robot just going straight (True or False): "))
px = 0
nx = 0
py = 0
px = 0
if IsStraight == True:
    distance = float(input("What the distance the robot went: "))
    if distance <= 12:
        px = distance * 0.1 / 12
        nx = distance * 0.1 / 12
        py = 0
        ny = distance * 0.1 / 12
    elif distance <=36:
        px = distance * 0.1 / 36
        nx = distance * 0.1 / 36
        py = 0
        ny = distance * 0.5 / 36
    elif distance <= 60:
        px = distance * 0.8 / 60
        nx = distance * 0.4 / 60
        py = 0
        ny = distance * 0.7 / 60
    else:
        px = distance * 1.3 / 96
        nx = distance * 0.2 / 96
        py = 0
        ny = distance * 1 / 96
    print("You went {0:.2f} inches with an error of {1:.2f} in the positive x and {2:.2f} in the negative x plus {3:.2f} in the Positive y and in the {4:.2f} negivative y".format(distance,px,nx,py,ny))
else:
    distance = float(input("What the distance the robot went after it made the turn: "))
    if distance <= 12:
        px = distance * 0.2 / 12
        nx = distance * 0.2 / 12
        py = distance * 0.2 / 12
        ny = distance * 0.4 / 12
    elif distance <=36:
        px = distance * 0.6 / 24
        nx = distance * 0.1 / 24
        py = distance * 0.1 / 24
        ny = distance * 0.8 / 24
    elif distance <= 60:
        px = distance * 0.6 / 48
        nx = distance * 0.1 / 48
        py = distance * 0.1 / 48
        ny = distance * 2.1 / 48
    else:
        px = distance * 1 / 96
        nx = distance * 0.1 / 96
        py = distance * .1 / 96
        ny =  distance * 7.6 / 96
    print("You went {0:.2f} inches after going 12 inches then turning 90 degrees with an error of {1:.2f} in the positive x and {2:.2f} in the negative x plus {3:.2f} in the Positive y and in the {4:.2f} negivative y".format(distance,px,nx,py,ny))
    
#make the equations between each interval