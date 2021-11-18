from djitellopy import tello
from time import sleep

#This drone will start facing due east

me = tello.Tello()

############ PARAMETERS ############
fSpeed = 112 # Forward/Backward cm/sec
lrspeed = 112 # Left/Right cm/sec
aSpeed = 26 # Angular Velocity, Degrees/sec
uSpeed = 26 # Up/Down cm/sec
####################################

me.connect()
sleep(.1)

me.takeoff()
sleep(.1)

me.move_up(183)
sleep(.1)

me.move_forward(155)
sleep(.1)

me.rotate_counter_clockwise(90)
sleep(.1)

me.move_forward(153)
sleep(.1)

me.rotate_clockwise(90)
sleep(.1)

me.move_down(106)
sleep(.1)

me.move_forward(91)
sleep(.1)

me.rotate_clockwise(90)
sleep(.1)

me.move_up(45)
sleep(.1)

me.move_forward()
sleep(.1)

me.rotate_counter_clockwise(90)
sleep(.1)

me.move_forward(183)
sleep(.1)

me.land()
