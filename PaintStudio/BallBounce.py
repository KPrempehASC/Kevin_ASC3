from random import *

x = 350
y = 350
ballDiam = randrange(35, 140)
xSpeed = randrange(1, 10)
ySpeed = randrange(1, 10)

def setup():
    size(700, 700)
    background(255, 255, 255)
    
def draw():
    global x, y, xSpeed, ySpeed
    background(255, 255, 255)
    noStroke()
    fill(255, 0, 0)
    ellipse(x, y, ballDiam, ballDiam)
    x += xSpeed
    y += ySpeed
   
    if x < (ballDiam / 2) or x > 700 - (ballDiam / 2):
        xSpeed *= -1
            
    if y < (ballDiam / 2) or y > 700 - (ballDiam / 2):
        ySpeed *= -1