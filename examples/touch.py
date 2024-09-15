import time
from adafruit_circuitplayground import cp


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)


cp.pixels.brightness = 0.3

while True:
    cp.pixels.fill(BLUE)

    if cp.touch_A1:
        cp.pixels[5] = RED
        cp.pixels[6] = RED
        cp.pixels[7] = RED
    if cp.touch_A2:
        cp.pixels[7] = RED
        cp.pixels[8] = RED
    if cp.touch_A3:
        cp.pixels[8] = RED
        cp.pixels[9] = RED
    if cp.touch_A4:
        cp.pixels[0] = RED
        cp.pixels[1] = RED
    if cp.touch_A5:
        cp.pixels[1] = RED
        cp.pixels[2] = RED
    if cp.touch_A6:
        cp.pixels[2] = RED
        cp.pixels[3] = RED
    if cp.touch_TX:
        cp.pixels[3] = RED
        cp.pixels[4] = RED
