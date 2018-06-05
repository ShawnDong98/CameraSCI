#!/sur/bin/python
#coding: utf8
#@date = '2018.5.6'
#@author = 'ShawnDong'

from SimpleCV import  *

myCamera = Camera()
myDisplay = Display()

while not myDisplay.isDone():
    frame = myCamera.getImage()
    frame.save(myDisplay)
