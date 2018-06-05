#/usr/bin/env/python2
# -*- coding: utf-8 -*-
#@date = '2018.5.31'
#@author = 'ShawnDong'

#---------------------------------

import requests
import json
import base64
import urllib
from aip import AipImageClassify, AipSpeech
import os
import time


#---------------------------------------------------------------------------
# The AI-Recognization Program
#---------------------------------------------------------------------------
def  get_access_token():
    APP_ID = '11150559'
    API_KEY = 'llfAqrRxdlzGGzjoZdTGecX3'
    SECRET_KEY = 'LgCrhLNLS6pMG2qLeYCzLYEW026WDnXB'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (API_KEY, SECRET_KEY)
    response = requests.post(host)
    access_token = response.content.decode('utf-8')
    access_token = json.loads(access_token)

    access_token = str(access_token['access_token'])

    return access_token, client

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def MarketRecognization(access_token,picture):
    url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/market?access_token=' + access_token
    header = {'Content-Type' : 'application/json'}
    image = get_file_content('/home/pi/pythoncode/%s' % (picture))
    image = base64.b64encode(image)
    body = {'image' : image, 'top_num': 1}
    body = json.dumps(body).encode('utf-8')
   # body = urllib.urlencode(body)

    response = requests.post(url,data=body,headers=header)
    response = json.loads(response.text)
    print(response)
    name = response['results'][0]['name']
    
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
