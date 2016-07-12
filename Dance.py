from Myro import *

s = 1

i = 0
while i < 2:
    turnBy(180)
    i = i + 1

forward(s, 1)
backward(s, 1)
turnBy(90)
forward(s,1)

j = 0
while j < 2:
    turnBy(180)
    j = j + 1

backward(s, 2)

k = 0
while k < 2:
    turnBy(180)
    k = k + 1