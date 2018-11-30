#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#echo server program
import socket

r1_ip = '10.10.2.2'
d_ip = '10.10.3.2' # IPv4 Address of Server
RCV_PORT = 25570  # PORT
r1_PORT = 25572


rcv_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
rcv_udp_sock.bind((r1_ip, RCV_PORT))

while 1:
    data,addr = rcv_udp_sock.recvfrom(1024)
    if data:
        print("router r1 get the message"),repr(data)
        dst_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        dst_udp_sock.sendto(data,(d_ip,r1_PORT))
         
      






