#!/sur/bin/python
# -*- coding: utf-8 -*-
#@date = '2018.6.13'
#@author = 'ShawnDong'
#--------------------------------------
#---------------------------------------------------
import os

#--------------------------------------------------
#Function: Get the commad line
#--------------------------------------------------
def GetCommand():
    command = "sudo iwlist wlan0 scan"
    r = os.popen(command)
    info = r.readlines()
    return info
    '''
    for line in info:
        line = line.strip('\r\n')
        print (line + "666")
    '''
#-------------------------------------------------
#Function: Find the target string
#-------------------------------------------------
def FindSubStr(substr, str, i):
    count = 0
    while i > 0:
        index = str.find(substr)
        if index == -1:
            return -1
        else:
            str = str[index+1:]
            i -= 1
            count = count + index + 1
    return count - 1

#-------------------------------------------------
#Function: Run Command and Find the key str
#Cnt : How many times the command excutes
#i   : How many times the TargetStr appers
#-------------------------------------------------
def RunAndFindStr(command,TargetStr, Cnt,i):
    r = os.popen(command)
    info = r.readlines()
    count = 0
    for j in range(0, Cnt):
        count = FindSubStr(TargetStr,str(info),i)
        print(count)
        if(count != -1):
            print("ok")
            return 1
            break
        if(count == -1 and j == Cnt-1):
            print("no")
            return 0

RunAndFindStr("sudo ifconfig","wlan0",10,1)
        
          
    
    

