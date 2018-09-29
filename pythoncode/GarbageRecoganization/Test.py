#/usr/bin/env/python2
# -*- coding: utf-8 -*-
#@date = '2018.4.23'
#@author = 'ShawnDong'

#---------------------------------

import requests
import json
import base64
import urllib
import os
import time

#------------------------------------------------
import picamera
from SimpleCV  import *
from SimpleCV.Display import Display

#------------------------------------------------

import RPi.GPIO as GPIO
from SteeringGear import *
from Compare import *


#---------------------------------------------------------------------------
# The AI-Recognization Program
#---------------------------------------------------------------------------
def  get_access_token():
    APP_ID = '11150559'
    API_KEY = 'llfAqrRxdlzGGzjoZdTGecX3'
    SECRET_KEY = 'LgCrhLNLS6pMG2qLeYCzLYEW026WDnXB'

    #client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (API_KEY, SECRET_KEY)
    response = requests.post(host)
    access_token = response.content.decode('utf-8')
    access_token = json.loads(access_token)

    access_token = str(access_token['access_token'])

    return access_token

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def GarbageRecognization(access_token,picture):
    url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/rubbish?access_token=' + access_token
    header = {'Content-Type' : 'application/json'}
    image = get_file_content('/home/pi/version/pythoncode/GarbageRecoganization/%s' % (picture))
    image = base64.b64encode(image)
    body = {'image' : image, 'top_num': 1}
    body = json.dumps(body).encode('utf-8')
   # body = urllib.urlencode(body)

    response = requests.post(url,data=body,headers=header)
    response = json.loads(response.text)
    print(response)
    L = []
    for r in response:
        L.append(r)
    if L[0] != 'error_code':
        if len(response['results']) != 0:
            name = response['results'][0]['name']
            
        else:
            name = 'default'
               
    else:
        name = 'default'
               
    return name

#------------------------------------------------------------------------------

def IfWIFI():
    a = os.popen("hostname -I")
    a = a.readline()
    if len(a) == 1:
        return 1
    else:
        return 0

#-------------------------------------------------------------------------------

def get_camera_image(name):
    with picamera.PiCamera() as camera:
        camera.start_preview()
        camera.capture(name)
        #time.sleep(5)
        camera.stop_preview()
    return Image(name)

#-----------------------------------------------
def file_name(file_dir):
    list =[]
    for root, dirs, files in os.walk(file_dir):
        list.append(files)

    return list


def destory():
    GPIO.cleanup()

def main():
    #os.system('sudo omxplayer /home/pi/Downloads/test.mp3')
    #time.sleep(8)
    #while (IfWIFI()):
        #print("No WIFI")
    picture = 'image6.jpg'
    while True:
        try:
            at = get_access_token()
            break
        except:
            continue
    setup()
    p=GPIO.PWM(13,300)
    p.start(15)
    time.sleep(1.5)
    q=GPIO.PWM(15,300)
    q.start(15)
    time.sleep(1.5)
    i = 0
    j = 0
    n = 0
    #RunTwo(p,q,40)
    #cam = Camera()
    #display = Display()
    while j < 5:
        get_camera_image('image%d.jpg'%j)
        '''
        frame = cam.getImage()
        #frame.save(display)
        frame.save('image%d.jpg'%j)
        '''
        time.sleep(0.5)
        j += 1
    img0 = cv2.imread("image0.jpg")
    img1 = cv2.imread("image1.jpg")
    img2 = cv2.imread("image2.jpg")
    img3 = cv2.imread("image3.jpg")
    img4 = cv2.imread("image4.jpg")
    diff0 = getdiff(img0)
    diff1 = getdiff(img1)
    diff2 = getdiff(img2)
    diff3 = getdiff(img3)
    diff4 = getdiff(img4)
    ss0 = getss(diff0)
    ss1 = getss(diff1)
    ss2 = getss(diff2)
    ss3 = getss(diff3)
    ss4 = getss(diff4)
    avrSS = (ss0 + ss1 + ss2 + ss3 + ss4) / 5
    os.system('sudo omxplayer /home/pi/Downloads/test.mp3')
    times = 0
    #while not display.isDone():
    while True:
            get_camera_image('image5.jpg')
            '''
            frame = cam.getImage()
            #frame.save(display)
            frame.save('image5.jpg')
            '''
            img5 = cv2.imread("image5.jpg")
            diff5 = getdiff(img5)
            ss5 = getss(diff5)
            error = abs(avrSS - ss5)
            print(error)
            if(error > 300):
                error = 0
                times += 1
                if(times == 2):
                    times = 0
                    print('ss1: %s' % avrSS)
                    print('ss2: %s' % ss5)
                    
                    time.sleep(2)
                    frame = get_camera_image('image6.jpg')
                    name = GarbageRecognization(at,picture)
                    print(name)
                    if name == "bottle":
                        print(name)
                        name = ''
                        RunTwo(p,q,70)
                        n = len(file_name("/home/pi/bottle")[0]) + 1
                        print("num: %s" % n)
                        frame.save('/home/pi/bottle/image%d.jpg'%n)
                        print("bottle")
                                
                    if name == "paper":
                        print(name)
                        name = ''
                        RunTwo(p,q,45)
                        n = len(file_name("/home/pi/paper")[0]) + 1
                        print("num: %s" % n)
                        frame.save('/home/pi/paper/image%d.jpg'%n)
                        print("paper")
                       
                    if  name == "[default]":
                        print(name)
                        name = ''
                        RunTwo(p,q,20)
                        n = len(file_name("/home/pi/default")[0]) + 1
                        print("num: %s" % n)
                        frame.save('/home/pi/default/image%d.jpg'%n)
                        print("default")
                    
            else:
                times = 0
            
                
    '''
    picture = 'lj.png'
    at = get_access_token()
    name = GarbageRecognization(at,picture)
    print(name)
    '''
#-----------------------------------------------
'''
def main():
    while (IfWIFI()):
        print("No WIFI")
    picture = 'shot.jpg'
    at,client = get_access_token()
    setup()
    p=GPIO.PWM(13,300)
    p.start(15)
    q=GPIO.PWM(15,300)
    q.start(15)
    time.sleep(2)
    cam = Camera()
    display = Display((800,600))
    while display.isNotDone():

        if InfraredDetect(12) == 0:
            print("detected")
            img = cam.getImage()
            img.save(picture)
            img.save(display)
            name = GarbageRecognization(at,picture)
            print(name)
            if name == "bottle":
                    RunTwo(p,q,40)
                    time.sleep(1)
            if name == "paper":
                    RunTwo(p,q,40)
                    time.sleep(1)
            if  name == "defaults":
                    RunTwo(p,q,40)
                    time.sleep(1)
'''
    
    


if __name__ == '__main__' :
    main()
