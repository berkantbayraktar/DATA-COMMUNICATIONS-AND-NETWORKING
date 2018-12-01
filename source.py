#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import socket
import sys
import time
import json

HOST = '10.10.1.2' # broker ip
PORT = 25574  # port number 

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect
s.connect((HOST,PORT))

# open file to be sent over the network
f = open("./demofile_light.txt","r")

while 1:
    # read 724 bytes from file
    message = f.read(724)
    # if end of file break
    if(len(message) == 0):
        break
        
    # create json object with timestamp and message
    data = {
        "message" : message, # 724 byte message from the file
        "timestamp": str(time.time()) # current time
    }
    #a = {"timestamp": str(time.time())} computed size 280
    if data:
        string_data = json.dumps(data) # turn json to string
        s.send(string_data) # send data
        print(string_data) # print the ack for debugging
        rcv_data = s.recv(1024) # receive ack from broker
        f_rcv_data = float(rcv_data)
        print('dest:', repr(f_rcv_data), 'now:',repr(time.time()), 'difference:', repr(time.time()- f_rcv_data))
        
        
# close tcp socket
s.close()