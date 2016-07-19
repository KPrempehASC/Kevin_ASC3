myColor = 0

def setup():
    size(1280, 720)
    background(255, 255, 255)
    
def mouseDragged():
    ellipse(mouseX, mouseY, 10, 10)

def draw():
    
    global myColor
    
    def squareRed():
        noStroke()
        fill(255, 0, 0)
        rect(0, 0, 160, 60)
        
    def squareBlue():
        noStroke()    
        fill(0, 0, 255)
        rect(160, 0, 160, 60)
        
    def squareYellow():
        noStroke()    
        fill(255, 255, 0)
        rect(320, 0, 160, 60)
        
    def squareGreen():
        noStroke()    
        fill(0, 255, 0)
        rect(480, 0, 160, 60)
        
    def squareOrange():
        noStroke()
        fill(255, 165, 0)
        rect(640, 0, 160, 60)
        
    def squarePurple():
        noStroke()
        fill(128, 0, 128)
        rect(800, 0, 160, 60)
             
    def squareWhite():
        fill(255, 255, 255)
        rect(960, 0, 160, 60)
        
    def squareBlack():
        noStroke()
        fill(0, 0, 0)
        rect(1120, 0, 160, 60)
                    
    squareRed()
    squareBlue()
    squareYellow()
    squareGreen()
    squareOrange()
    squarePurple()
    squareWhite()
    squareBlack()
    
    fill(0)
    
    if mouseButton == LEFT:
        if mouseY < 60:
            if mouseX < 160:
                myColor = 1
            elif mouseX < 320:
                myColor = 2
            elif mouseX < 480:
                myColor = 3
            elif mouseX < 640:
                myColor = 4
            elif mouseX < 800:
                myColor = 5
            elif mouseX < 960:
                myColor = 6 
            elif mouseX < 1120:
                myColor = 7
            elif mouseX < 1280:
                myColor = 0
        if mouseY > 60:
           if myColor == 1:
               fill(255, 0, 0)
           if myColor == 2:
               fill(0, 0, 255)
           if myColor == 3:
               fill(255, 255, 0)
           if myColor == 4:
               fill(0, 255, 0)
           if myColor == 5:
               fill(255, 165, 0)
           if myColor == 6:
               fill(128, 0, 128)
           if myColor == 7:
               fill(255, 255, 255)
               ellipse(mouseX, mouseY, 50, 50)
           if myColor == 0:
               fill(0, 0, 0)                
        mouseDragged()