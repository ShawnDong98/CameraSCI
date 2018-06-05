#/usr/bin/env/python2
# -*- coding: utf-8 -*-
#@date = '2018.4.23
#@author = 'ShawnDong'

#---------------------------------

import requests
import json
import base64
import urllib

from SimpleCV  import *
from SimpleCV.Display import Display

def  get_access_token():
    APP_ID = '11141534'
    API_KEY = 'ciyxEBEcvg623GasZqDmMl6j'
    SECRET_KEY = 'gNI5ttvKfCprkAPT8r8vlON9awAQrvHL'

    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (API_KEY, SECRET_KEY)
    response = requests.post(host)
    access_token = response.content.decode('utf-8')
    access_token = json.loads(access_token)

    access_token = str(access_token['access_token'])

    return access_token

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def FaceRecognization(access_token,picture):
    url = 'https://aip.baidubce.com/rest/2.0/face/v2/detect?access_token=' + access_token
    header = {'Content-Type' : 'application/x-www-form-urlencoded'}
    image = get_file_content('/home/pi/pythoncode/%s' % (picture))
    image = base64.b64encode(image)
    body = {'image' : image}
    body = urllib.urlencode(body)

    response = requests.post(url,data=body,headers=header)
    response = json.loads(response.text)
    location = response['result'][0]['location']
    
    return location
    

def main():
    picture = 'shot.png'
    at = get_access_token()
    cam = Camera()
    display = Display((800,600))
    while display.isNotDone():
         img = cam.getImage()
         img.save(picture)
         img.save(display)
         content = FaceRecognization(at,picture)
         print(content)
         print(content['height'])
'''
         facelayer = DrawingLayer((frame.width, frame.height))
         w = face.width()
         h = face.height()
        
         facebox_dim = (w,h)
         facebox = facelayer.centeredRectangle(face.coordinates(), facebox_dim)

         img.addDrawingLayer(facelayer)
         img.applyLayers()
            '''
     
        

if __name__ == '__main__' :
    main()
