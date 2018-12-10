
from sense_hat import SenseHat
from random import randint
from time import sleep
sense = SenseHat()
while True:
    x = randint(0,7)
    y = randint(0,7)
    r = randint(0,225)
    g = randint(0,225)
    b = randint(0,225)
    sense.set_pixel(x, y, r, g, b)

