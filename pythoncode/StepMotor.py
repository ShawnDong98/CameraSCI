#/usr/bin/env/python2
# -*- coding: utf-8 -*-
#@date = '2018.4.24'
#@author = 'ShawnDong'

#---------------------------------

import RPi.GPIO as GPIO
import time
from array import *

IN1 = 40
IN2 = 38
IN3 = 36
IN4 =35

def setStep(w1, w2, w3, w4):
    GPIO.output(IN1, w1)
    GPIO.output(IN2, w2)
    GPIO.output(IN3, w3)
    GPIO.output(IN2, w3)

def stop():
    setStep(0, 0, 0, 0)

def forward(delay, steps):
    for i in range(0, steps):
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)

def backward(delay, steps):
    for i in range(0, steps):
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(1, 0, 0, 0)
        time.sleep(delay)

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

def loop():
    while True:
        print "backward..."
        backward(0.003, 512)

        print "stop..."
        stop()
        time.sleep(3)

        print "forward..."
        forward(0.005, 512)

        print "stop..."
        stop()
        time.sleep(3)

def run(steps,clockwise):
    ports = [40,38,36,35]
    arr = [0,1,2,3];
    if clockwise != 1:
        arr = [3,2,1,0];
    for x in range(0, steps):
        for j in arr:
            time.sleep(0.01)
            for i in range(0,4):
                if i == j:
                    GPIO.output(ports[i],True)
                else:
                    GPIO.output(ports[i],False)

def destory():
    GPIO.cleanup()

def main():
    setup()
    try:
        run(45, 0)
    except KeyboardInterrupt:
        detroy()

if __name__ == '__main__':
    main()
    
        
