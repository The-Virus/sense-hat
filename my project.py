
from sense_hat import SenseHat
from random import randint
from time import sleep
sense = SenseHat()




def first_quadrant():
    x = randint(d,e)
    y = randint(d,e)
    r = (255)
    g = randint(100,255)
    b = randint(0,255)
    sense.set_pixel(x, y, r, g, b)

while True:
    for i in range(2560):
        d=0
        e=3
        first_quadrant()
    sense.clear()
    for i in range(2560):
        d=4
        e=7
        first_quadrant()
    sense.clear()
    for i in range(2560):
        d=1
        e=6
        first_quadrant()
    sense.clear()
    for i in range(2560):
        d=2
        e=5
        first_quadrant()
    sense.clear()
    for i in range(2560):
        d=3
        e=4
        first_quadrant()
    sense.clear()
    for i in range(2560):
        d=2
        e=5
        first_quadrant()
    sense.clear()
    for i in range(2560):
        d=1
        e=6
        first_quadrant()
    sense.clear()
    
    
