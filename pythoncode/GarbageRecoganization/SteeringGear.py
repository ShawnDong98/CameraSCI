#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@date = '2018.5.28'
#@author = 'ShawnDong'

#--------------------------------------------------
import RPi.GPIO as GPIO
import time
from array import *
import sys

#---------------------------------------------------------
#The StepperMoter Program
#----------------------------------------------------------




#------------------------------------------------

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)

#------------------------------------------------



def RunTwo(p,q,angle):
       q.ChangeDutyCycle(angle)
       time.sleep(2.5)
       p.ChangeDutyCycle(35)
       time.sleep(2.5)
       p.ChangeDutyCycle(15)
       time.sleep(2.5)
       q.ChangeDutyCycle(15)
       time.sleep(2.5)



def main():

    setup()
    p=GPIO.PWM(13,300)
    p.start(15)
    q=GPIO.PWM(15,300)
    q.start(15)
    time.sleep(2.5)
    angle = float(sys.argv[1])
    RunTwo(p,q,angle)
    time.sleep(1)


if __name__ == "__main__":
    main()




