# -*- coding: utf-8 -*- 

import socket

r1_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
r2_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

HOST = '127.0.0.1'
R1_PORT = 19073
R2_PORT = 19074

r1_udp_sock.bind((HOST, R1_PORT))
r2_udp_sock.bind((HOST, R2_PORT))

while 1 : 
    data_r1,addr_r1 = r1_udp_sock.recvfrom(1024)
    data_r2,addr_r2 = r2_udp_sock.recvfrom(1024)

    if data_r1:
        print 'destination got the message from r1 ' ,repr(data_r1)
    if data_r2:
        print 'destination got the message from r2', repr(data_r2)

