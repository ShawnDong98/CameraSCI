#!/sur/bin/python
#coding: utf8
import snowboydecoder
import sys
import signal
from AIBox import *
from SimpleCV import  *

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

def RecVoice():
    os.system('mplayer /home/pi/pythoncode/AIBox/JarvisAnswer.mp3')
    os.system('arecord -d 5 -r 16000 -f S16_LE temp.wav')
    os.system('aplay temp.wav')
    at, client = get_access_token()
    result = VoiceRecognization(client)
    result = result['result'][0].encode('utf-8')

    print(result)
    print(result.find('温湿度'))

def main():

    if len(sys.argv) == 1:
        print("Error: need temp.wavo specify model name")
        print("Usage: python demo.py your.model")
        sys.exit(-1)

    model = sys.argv[1]

    # capture SIGINT signal, e.g., Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
    print('Listening... Press Ctrl+C to exit')

    detector.start(detected_callback=GetTemHumVoice,
                    interrupt_check=interrupt_callback,
                    sleep_time=0.03)

    detector.terminate()

if  __name__ == '__main__':
    main()



