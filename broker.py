#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import socket
from random import randint


broker_ip = '127.0.0.1'
router_ip = '127.0.0.1'
tcp_port = 19070
udp1_port = 19071
udp2_port = 19072


tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((broker_ip, tcp_port))
tcp_socket.listen(1)
conn,addr = tcp_socket.accept()

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1 : 
    
    data = conn.recv(1024)

    if data : 
        print("received from client"),repr(data)
        rand = randint(0, 1)
        sack = 'aldim panpa'
        conn.sendall(ack)
        if rand == 1 : 
            udp_socket.sendto(data,(router_ip,udp1_port))
        else :
            udp_socket.sendto(data,(router_ip,udp2_port))

conn.close()  
