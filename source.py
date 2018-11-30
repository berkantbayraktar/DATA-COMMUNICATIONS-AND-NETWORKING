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

while True:
    message = f.read(500)
    if message == '':
        break
    data = {
        "message" : message,
        "timestamp": str(time.time())
    }
    if data:
        # turn json to string and send
        json_data = json.dumps(data)
        s.send(json_data) 
        #rcv_data = s.recv(1024)
        print ("Sent" + json_data)

s.shutdown(socket.SHUT_RDWR)
s.close()