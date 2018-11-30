#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#echo server program
import socket

HOST = '127.0.0.1' # IPv4 Address of Server
RCV_PORT = 19072  # PORT
DST_PORT = 19074


rcv_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
rcv_udp_sock.bind((HOST, RCV_PORT))

while 1:
    data,addr = rcv_udp_sock.recvfrom(1024)
    if data:
        print("router r2 get the message"),repr(data)
        dst_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        dst_udp_sock.sendto(data,(HOST,DST_PORT))
        






