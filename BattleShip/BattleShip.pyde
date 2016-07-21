from random import *

board = []
boardSize = 5
x = 0
yCor = 0
z = x - 1
    
def setup():
    size(boardSize * 100, boardSize * 100 + 50)
    
    global x, y, yCor, boardSize
    
    for i in range(boardSize):
        board.append([0] * boardSize)
        
    for i in range(boardSize - 2):
        board[(int(randrange(boardSize)))][(int(randrange(boardSize)))] = "S" 
             
    print(board)

def draw():
    global x, yCor, boardSize
    while x < boardSize:
        for i in range(len(board[x])):
            if(board[x][i] == 0 or "S"):
                for i in range(boardSize):
                    stroke(0, 255, 0)
                    strokeWeight(0.35)
                    fill(0, 0, 255)
                    rect(i * 100, yCor, 100, 100)
                    
            yCor += 100
            x += 1
                
    if (mouseButton == LEFT):
        global z
        xPos = int(mouseX/100)
        yPos = int(mouseY/100)
        #if 0 < xPos < boardSize and 0 < yPos < boardSize:
        for i in range(len(board[z])):
            if(board[xPos][yPos] == "S"):
                stroke(0, 0, 255)
                strokeWeight(0.35)
                fill(255, 0, 255)
                rect(xPos * 100, yPos * 100, 100, 100)
                
            else:
                stroke(0, 0, 255)
                strokeWeight(0.35)
                fill(255, 0, 0)
                rect(xPos * 100, yPos * 100, 100, 100)