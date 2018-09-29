#!/usr/bin/env python  
#encoding: utf-8  
#description: get local ip address 
import socket, fcntl, struct
import array
from datetime import datetime
import smtplib
import os
#from email.mine.text import MIMEText

def get_ip_address():

    #先获取所有网络接口
    SIOCGIFCONF = 0x8912
    SIOCGIFADDR = 0x8915
    BYTES = 4096         
    sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    names = array.array('B',b'\0' * BYTES)
    bytelen = struct.unpack('iL', fcntl.ioctl(sck.fileno(), SIOCGIFCONF, struct.pack('iL', BYTES, names.buffer_info()[0])))[0]
    namestr = names.tostring()
    ifaces = [namestr[i:i+32].split('\0', 1)[0] for i in range(0, bytelen, 32)]
    
    #再获取每个接口的IP地址
    iplist = []
    for ifname in ifaces:
        ip = socket.inet_ntoa(fcntl.ioctl(sck.fileno(),SIOCGIFADDR,struct.pack('256s',ifname[:15]))[20:24])
        iplist.append(ip)
       # iplist.append(ifname+':'+ip)
    return iplist

if __name__ == '__main__':
    result = get_ip_address()
    print(result)
    print(len(result))

    while True:
        if len(result) == 1:
            os.system('sudo create_ap wlan0 eth0 MyAccessPoint MyPassPhrase')
            break

        


