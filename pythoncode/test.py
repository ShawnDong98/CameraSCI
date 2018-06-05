from SimpleCV  import *
from SimpleCV.Display import Display
t = 0
cam = Camera()
display = Display((800,600))
while display.isNotDone():
    t=t+1
    img = cam.getImage()
    img.save('bottle'+str(t)+'.jpg')
    img.save(display)
'''
    if t==30:
        break
'''
