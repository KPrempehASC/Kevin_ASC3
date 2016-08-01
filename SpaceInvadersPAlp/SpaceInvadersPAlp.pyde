aliens = [["1","1","1","1","1"],
         ["1","1","1","1","1"],
         ["1","1","1","1","1"],
         ["1","1","1","1","1"],
         ["1","1","1","1","1"]]

#This is for the tank
tankX = 400
tankY = 450
tank_spd = 3

# For the bullet 
bulletX = tankX + 25
bulletY = tankY - 15
bulletFired = False
XSpeed = 1
YSpeed = -5

#This if for the aliens
alien_Xspd = .2
alienX = 75
alienY = 0

#This creates the tank
def tank():
    background(0, 0, 0)
    noStroke()
    fill(0, 255, 0)
    ellipse(tankX + 25, tankY, 50, 15) #Top Rectangle
    rect(tankX, tankY, 50, 15) #Bottom Rectangle
    rect(tankX + 21.5, tankY - 15, 7, 10) #Cannon

#This is makes the screen
def setup():
    size(500, 500)
    background(0, 0, 0)
    
# This makes the bullet 
def bullet():
    global tankX, bulletX, bulletY, YSpeed, bulletFired
    if bulletFired == True:    
        fill(0, 255, 0)
        ellipse(bulletX, bulletY, 7, 7)
        bulletY += YSpeed
        if bulletY == 5:
            bulletFired = False
    
#This makes the aliens
def draw():
    tank()
    bullet()
    
    global aliens, alien_Xspd, alienX, alienY, bulletFired, bulletX, bulletY
    for r in range(len(aliens)):
        for e in range(len(aliens)):
            if(aliens[r][e] == "1"):
                fill(255)
                rect(r*75 + alienX, e*50 + alienY , 40, 30)

            if bulletY == alienY:
                print("Inside BulletY")
                if bulletX > alienX and bulletX < alienX + 40:
                    print("Inside BulletX")
                    aliens[r][e] = "0"
                    bulletFired = False
                
        '''alienX += alien_Xspd
        if alienX < 0 or alienX > 150:
            alienY += 2.5
            alien_Xspd *= -1'''
                
                
                
            
            

        
        
#This is for an action to be performed when a key is pressed    
def keyPressed():
    global tankX, bulletFired, tankY, bulletX, bulletY, Yspeed, Xspeed
    #print("pressed %s %d" % (key, keyCode))
    if keyCode == 39 and tankX < 425:
            tankX +=10
    if keyCode == 37 and tankX > 25:
            tankX -=10
    if keyCode == 32 and bulletFired == False:
        bulletX = tankX + 25
        bulletY = tankY - 15
        bulletFired = True
        