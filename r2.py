#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#echo server program
import socket

r2_ip = '10.10.4.2'
d_ip = '10.10.3.2' # IPv4 Address of Server
RCV_PORT = 25570  # PORT
r2_PORT = 25573


rcv_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
rcv_udp_sock.bind((r2_ip, RCV_PORT))

while 1:
    data,addr = rcv_udp_sock.recvfrom(1024)
    if data:
        print("router r2 get the message"),repr(data)
        dst_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        dst_udp_sock.sendto(data,(d_ip,r2_PORT))
        






