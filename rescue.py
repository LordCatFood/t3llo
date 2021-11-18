from djitellopy import tello
from time import sleep

#This drone will start facing due east

me = tello.Tello()

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
