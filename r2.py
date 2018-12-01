#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#echo server program
import socket

r2_ip = '10.10.4.2' # router2 ip
d_ip = '10.10.3.2' # destination ip
RCV_PORT = 25570  # port number for receiving
r2_PORT = 25573   # port number for sending

# create socket for receiving from broker
rcv_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
rcv_udp_sock.bind((r2_ip, RCV_PORT))

#create socket for sending to destination
dst_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

while 1:
    # receive 1024 byte data from broker
    data,addr = rcv_udp_sock.recvfrom(1024)
    # if data is valid
    if data:
        # send data to destination
        dst_udp_sock.sendto(data,(d_ip,r2_PORT))
        






