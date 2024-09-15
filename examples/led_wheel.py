import time

from adafruit_circuitplayground import cp


RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

colors = [RED, PURPLE, BLUE, CYAN, GREEN, YELLOW]


red = 255
green = 0
blue = 0

while True:
    for color in colors:
        for i in range(0, 10):
            cp.pixels[i] = color
            time.sleep(0.1)
