from random import *

def setup():
    size(1280, 720)

def draw():
    ellipse(mouseX, mouseY, randrange(1, 100), randrange(1, 100))
    fill(randrange(0, 255), randrange(0, 255), randrange(0, 255))