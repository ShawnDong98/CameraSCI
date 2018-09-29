#/usr/bin/env python
# -*- coding: utf-8 -*-
#@date = '2018.5.28'
#@author = 'ShawnDong'

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO_OUT = 12

GPIO.setwarnings(False)
GPIO.setup(GPIO_OUT,GPIO.IN)

def  InfraredDetect(GPIO_OUT):
        if GPIO.input(GPIO_OUT) == 0:
                return 0
        else:
                return 1
