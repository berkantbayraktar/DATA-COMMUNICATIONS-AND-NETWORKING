#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#echo server program
import socket

HOST = '127.0.0.1' # IPv4 Address of Server
PORT = 19071  # PORT

udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
udp_sock.bind((HOST, PORT))

while 1:
    data = udp_sock.recvfrom(1024)
    if data:
        print 'router r1 get the message ' ,repr(data)





