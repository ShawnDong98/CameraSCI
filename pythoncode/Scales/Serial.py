#/usr/bin/env/python2
# -*- coding: utf-8 -*-
#@date = '2018.5.29'
#@author = 'ShawnDong'

#--------------------------------------

import serial
import time
from MarketRecoganization import *

#------------------------------------------------
from SimpleCV  import *
from SimpleCV.Display import Display

#-------------------------------------------------

ser = serial.Serial('/dev/ttyAMA0',9600)
'''
picture = 'shot.jpg'
at,client = get_access_token()
name = MarketRecognization(at,picture)
print(name)
'''
def main():
    while (IfWIFI()):
        print("No WIFI")
    picture = 'shot.jpg'
    at,client = get_access_token()
    cam = Camera()
    display = Display((800,600))
    a = 1
    b = 0
    while display.isNotDone():
        count = ser.inWaiting()
        if count != 0:
            recv = ser.read(count)
            print(type(recv))
            if recv[0] == '*' and recv[-1] == '#':
                print("detected")
                img = cam.getImage()
                img.save(picture)
                img.save(display)
                name = MarketRecognization(at,picture)
                print(name)
                if name == "Bread":
                        b = 1
                if name == "Cookies":
                        b = 2
                if  name == "HotStrips":
                        b = 3 
                if name == "Sepals":
                        b = 4
                if name == "EggRolls":
                        b = 5
                if  name == "Beans":
                        b =6
                ser.write("*,%s,%s,#"%(a,b)) 
        ser.flushInput()
        time.sleep(0.1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()
#'''
