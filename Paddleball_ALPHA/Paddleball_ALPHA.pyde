from random import *

x = 640
y = 360
xSpeed = 3
ySpeed = 3
paddleY = 675
score = 0
gameover = False
brickX = 640
brickY = 180
#hardMode = False

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
    global x, y, xSpeed, ySpeed, paddleY, gameover, score
    background(255, 255, 255)
    noStroke()
    fill(0, 0, 0)
    ball = ellipse(x, y, 15, 15)
    paddle = rect(mouseX, paddleY, 100, 10)
    #bossBrick()
    x += xSpeed
    y += ySpeed
    
    textSize(15)
    fill(0, 0, 0)
    text(score, 5, 15)
    if x < 7.5 or x > 1272.5:
        xSpeed *= -1
    if y < 7.5:
        ySpeed *= -1
        
    '''if (brickX - (brickX / 2)) <= x <= ((brickX / 2) + brickX):
        #if y >= brickY:
            #hitBossBrick()
            ySpeed *= -1
        else:    
            ySpeed *= 1'''    
        
    if y >= paddleY:
        if mouseX <= x <= (100 + mouseX):
            if y > paddleY:
                ySpeed *= 1
                gameover = True
            else:    
                ySpeed *= -1
                score += 10
                
    if gameover == True:
        score = str(score)
        textSize(48)
        fill(0, 0, 0)
        text("GAME OVER, BUDDY.", 400, 260)
        textSize(24)
        text("I guess you just gave up. This is an easy game, you know?", 300, 290) 
        text("Such a shame...", 540, 314)
        text("Welp. At least you got " + score + " points.", 455, 370)
        
        '''if score >= 50:
            textSize(18)
            
        elif score >= 100:
            textSize(18)
            text("Heh, you're pretty good. Why dont you try the Hard Mode?")'''
                     
        
        