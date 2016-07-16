from Myro import *

obamaDarkBlue = (0, 51, 76)
obamaRed = (217, 26, 33)
obamaBlue = (112, 150, 158)
obamaYellow = (252, 227, 166)

pic = makePicture(pickAFile())

for pixel in getPixels(pic):
    gray = getBlue(pixel)
    if gray > 180:
        setRGB(pixel, obamaYellow)
    elif gray > 120:
        setRGB(pixel, obamaBlue)
    elif gray > 60:
        setRGB(pixel, obamaRed)
    else:
        setRGB(pixel, obamaDarkBlue)

show(pic)