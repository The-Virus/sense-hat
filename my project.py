
from sense_hat import SenseHat
from random import randint
from time import sleep
sense = SenseHat()
while True:
    x = randint(4,7)
    y = randint(4,7)
    r = (255)
    g = randint(100,255)
    b = randint(0,255)
    sense.set_pixel(x, y, r, g, b)


    

