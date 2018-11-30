#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import socket
import sys
import time
import json

HOST = '127.0.0.1'
PORT = 19070   

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

f = open("./demofile.txt","r")

while 1:
    message = f.read(724)
    if(len(message) == 0):
        break
        
    data = {
        "message" : message,
        "timestamp": str(time.time())
    }
    #a = {"timestamp": str(time.time())} computed size 280
    if data:
        string_data = json.dumps(data)
        s.send(string_data) # turn json to string and send
        #rcv_data = s.recv(1024)
        print(string_data)
        

s.shutdown(socket.SHUT_RDWR)
s.close()