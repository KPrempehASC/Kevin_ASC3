def drawMickMouse():
    #basic outline
    fill(0, 0, 0)
    ellipse(90, 110, 150, 140)
    ellipse(310, 110, 150, 140)
    ellipse(200, 250, 230, 230)

    #eye whites
    noStroke()
    fill(255, 255, 255)    
    ellipse(165, 230, 100, 160)
    ellipse(235, 230, 100, 160)

    #eyes
    fill(0, 0, 0)
    ellipse(180, 230, 23, 70)
    ellipse(220, 230, 23, 70)

    #lower whites
    fill(255, 255, 255)
    rotate(0.45)
    ellipse(285, 208, 160, 93)
    rotate(-0.9)
    ellipse(75, 382, 160, 93)

    #nose
    fill(255, 255, 255)
    rotate(0.45)
    ellipse(200, 280, 95, 45)
    fill(0, 0, 0)
    ellipse(200, 280, 50, 30)
    
    #mouth
    stroke(0, 0, 0)
    strokeWeight(1.5)
    fill(255, 255, 255, 1)
    curve(105, 15, 120, 290, 280, 290, 295, 15)
    #curve(105, 15, 120, 290, 280, 290, 105, 15)

def setup():
    size(400, 400)
    background(255, 255, 0)
    
def draw():
    background(255, 255, 0)
    drawMickMouse()