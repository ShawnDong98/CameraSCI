#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@date = '2018.9.27'
#@author = 'ShawnDong'

#---------------------------------

from SteeringGear import *

def TakeOut(p,q,angle):
       q.ChangeDutyCycle(angle)
       time.sleep(2.5)
       p.ChangeDutyCycle(35)
       time.sleep(2.5)


def main():

    setup()
    p=GPIO.PWM(13,300)
    p.start(15)
    q=GPIO.PWM(15,300)
    q.start(15)
    time.sleep(2.5)
    angle = float(sys.argv[1])
    TakeOut(p,q,angle)
    time.sleep(1)


if __name__ == "__main__":
    main()
