#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import socket
from random import randint


broker_ip = '10.10.1.2'
router_ip_1 = '10.10.2.2'
router_ip_2 = '10.10.4.2'
tcp_port = 25570
udp1_port = 25572
udp2_port = 25573


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
        ack = 'aldim panpa'
        conn.sendall(ack)
        if rand == 1 : 
            udp_socket.sendto(data,(router_ip_1,udp1_port))
        else :
            udp_socket.sendto(data,(router_ip_2,udp2_port))

conn.close()  
