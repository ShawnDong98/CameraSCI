#!/sur/bin/python
# -*- coding: utf-8 -*-
#@date = '2018.5.07'
#@author = 'ShawnDong'

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

#---------------------------------------------------------------------
#Function: Main Function
#--------------------------------------------------------------------

def main():
    
    info = GetCommand()
    TargetInfo = str(info)
    print(type(TargetInfo))
    #string = "\xE5\x93\x88\xE5\x93\x88\xE5\x93\x88"
    #print(type(string))
    #print(string)
    count = 0
    count2 = 0
    i = 1
    j = 1
    
    while count != -1:
        count = FindSubStr("ESSID",TargetInfo,i)
        i += 1
        InfoTemp = TargetInfo[count:]
        count1 = FindSubStr(r"\n",InfoTemp,1)
        InfoTemp = InfoTemp[7:count1-1]
        while count2 != -1:
            count2 = FindSubStr(r"\x",InfoTemp,j)
            if count2 == -1 or count2 == -2:
                continue
            else:
                j += 1
                InfoTemp = InfoTemp[0:count2] + InfoTemp[count2+1:]
                #print(type(InfoTemp))
                #print(InfoTemp)
        count2 = -2
        j = 1
        #print(type(InfoTemp))
        print (InfoTemp)

#------------------------------------------------------------------------------------
        
if __name__ == "__main__":
    main()

