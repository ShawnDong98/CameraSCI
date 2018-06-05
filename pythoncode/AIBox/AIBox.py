#!/sur/bin/python
#coding: utf8
#@date = '2018.4.29'
#@author = 'ShawnDong'

#--------------------------------

from dht11 import *
from AISpeech import *
import os

import snowboydecoder

#------------------------------------------------------------------------------
def GetTemHumVoice():
    at, client = get_access_token()
    while True:
        Tem, Hum = GetTemHum()
        if Tem == "111" and Hum == "111":
            continue
        else:
            SyntheticSpeech('当前温度%s摄氏度,当前湿度百分之%s' % (Tem, Hum),client)
            os.system('mplayer /home/pi/pythoncode/AIBox/JarvisAnswer.mp3')
            break

def main():
    at, client = get_access_token()
#    SyntheticSpeech('您好,请问您需要什么服务',client)
#   os.system('mplayer /home/pi/pythoncode/AIBox/JarvisAnswer.mp3')
    '''
    while True:
        Tem, Hum = GetTemHum()
        if Tem == "111" and Hum == "111":
            continue
        else:
            SyntheticSpeech('当前温度%s摄氏度,当前湿度百分之%s' % (Tem, Hum),client)
            os.system('mplayer /home/pi/pythoncode/AIBox/audio.mp3')
    '''

if __name__ == '__main__':
    pass
    #main()

