#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@data = '2018.4.21'
#@author = 'Shawn Dong'

#----------------------

import requests
import json
import base64
import urllib
from aip import AipImageClassify, AipSpeech
import os
import time

#---------------------------------------------------------------------------
#PlantRecognization
#----------------------------------------------------------------------------
def get_access_token():
     #这里添上自己的app数据就ok
     APP_ID = '11150559'
     API_KEY = 'llfAqrRxdlzGGzjoZdTGecX3'
     SECRET_KEY = 'LgCrhLNLS6pMG2qLeYCzLYEW026WDnXB'

     client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

     url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (API_KEY, SECRET_KEY)
     response = requests.post(url)

     access_token = response.content.decode('utf-8')
     access_token = json.loads(access_token)

     access_token = str(access_token['access_token'])

     return access_token, client

def get_file_content(filePath):
     with open(filePath,'rb') as fp:
          return fp.read()

def get_recognization(access_token):
     host = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/plant?access_token=' + access_token
     header = {'Content-Type' : 'application/x-www-form-urlencoded'}

     #这里改成自己的文件路径
     image = get_file_content('/home/pi/pythoncode/caomei.jpg')
     image = base64.b64encode(image)
     body = {'image' : image, 'top_num' : 1}
     body = urllib.urlencode(body)

     response = requests.post(host,data=body,headers=header)
     response = json.loads(response.text)
     name = response['result'][0]['name']

     return name


def playsound(path):
    clip = mp3play.load(path)
    clip.play()
    time.sleep(5)
    clip.stop()

def main():
     time.sleep(20)
     at, client = get_access_token()
     recognization = get_recognization(at)
     
     print(type(recognization))
     result  = client.synthesis('这是一个'+recognization.encode('utf-8'), 'zh', 1, {
         'vol': 5, 'per': 4,
         })

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
     if not isinstance(result, dict):
         with open('auido.mp3', 'wb') as f:
             f.write(result)
             
     os.system('mplayer /home/pi/pythoncode/auido.mp3')
     

if __name__ == '__main__':
     main()
