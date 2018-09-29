import picamera
from SimpleCV import *
import time
import threading



def get_camera_image():
    with picamera.PiCamera() as camera:
        camera.start_preview()
        camera.capture('tmp.jpg')
        time.sleep(11000)
        camera.stop_preview()
    return Image('tmp.jpg')

                       
def file_name(file_dir):
    list =[]
    for root, dirs, files in os.walk(file_dir):
        list.append(files)

    return list

def initTimer():
    global timer

    print("Timer Clock")
    timer = threading.Timer(20.0, initTimer)
    timer.start()

timer = threading.Timer(20.0, initTimer)
timer.start()

#print(len(file_name("/home/pi/default")[0]))
#print(file_name("/home/pi/default"))
#get_camera_image()
'''
for i in range(20):
    img = get_camera_image()
    n = len(file_name("/home/pi/paper")[0]) + 1
    print("num: %s" % n)
    img.save("/home/pi/paper/img%d.jpg"%n)
'''
