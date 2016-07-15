from random import *

listA = ["Enter The", "Rise Of The", "Revenge Of The", "The Furious and", "The", "Escape From", "The Legend Of", "When", "Aquaman:", "War Of"]
listB = ["Imminent", "Amazing", "Malevolent", "Malicious", "Incredible", "Raging", "Gigantic", "Lethal", "Good", "The Absolute"]
listC = ["Dragon", "Empire", "AI", "Pokemon", "Loch Ness Monster", "Despair", "Cartoons", "Trolls", "Illuminati", "Samurai"]
listD = ["", "", "2", "", "", "", "", "3", "", ""]

i = 0
while i < 10:
    x = randrange(0, len(listA))
    y = randrange(0, len(listB))
    z = randrange(0, len(listC))
    a = randrange(0, len(listD))
    print(listA[x], listB[y], listC[z], listD[a])
    i = i + 1