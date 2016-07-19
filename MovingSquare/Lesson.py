BOB = 0
def setup():
    size(400,400)
    
def draw():
    global BOB
    global dir
    if  BOB > 40:
        dir = 1
    if BOB < 10:
        dir = 0
        
    if dir == 0:
        BOB = BOB - 1
    else:
        BOB = BOB += 1
    rect(200, 200, 50, 50)