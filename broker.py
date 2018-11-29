#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import socket



broker_ip = '127.0.0.1'
router_ip = '127.0.0.1'
tcp_port = 19070
udp_port = 19071


tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((broker_ip, tcp_port))
tcp_socket.listen(1)
conn,addr = tcp_socket.accept()

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1 : 
    
    data = conn.recv(1024)
    if data : 
        print 'received from client',repr(data)
        udp_socket.sendto(data,(router_ip,udp_port))
    else:
        print 'hello'



