from random import *

x = 640
y = 360
xSpeed = 3
ySpeed = 3
paddleY = 675
#score = 0
#gameOver = False
brickX = 640
brickY = 180

def bossBrick():
    stroke(0)
    strokeWeight(2)
    fill(255, 0, 0)
    boss = rect(320, 0, brickX, brickY)
    if brickX < 64 and brickY < 18:
        del(boss)
    
def hitBossBrick():
    global brickX, brickY
    brickX -= (brickX / 10)
    brickY -= (brickY / 10)

def setup():
    size(1280, 720)
    background(255, 255, 255)

def draw():
    global x, y, xSpeed, ySpeed, paddleY
    background(255, 255, 255)
    noStroke()
    fill(0, 0, 0)
    ball = ellipse(x, y, 15, 15)
    paddle = rect(mouseX, paddleY, 100, 10)
    bossBrick()
    x += xSpeed
    y += ySpeed
    
    #print(score)
    if x < 7.5 or x > 1272.5:
        xSpeed *= -1
    if y < 7.5:
        ySpeed *= -1
        
    if (brickX - (brickX / 2)) <= x <= ((brickX / 2) + brickX):
        if y >= brickY:
            hitBossBrick()
            ySpeed *= -1
                #gameover = True
        else:    
            ySpeed *= 1
                #score += 10 
                #print(score)    
        
    if y >= paddleY:
        if mouseX <= x <= (100 + mouseX):
            if y > paddleY:
                ySpeed *= 1
                #gameover = True
            else:    
                ySpeed *= -1
                #score += 10 
                #print(score)
                     
        
        