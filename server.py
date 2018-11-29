#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#echo server program
import socket

HOST = '127.0.0.1' # IPv4 Address of Server
PORT = 19071  # PORT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
s.bind((HOST, PORT))
s.listen(1)
conn,addr = s.accept()
print 'Client is connected with address: ',addr 
while 1:
    data = conn.recv(1024)
    print 'received from client',repr(data)
    if data:
        conn.sendall(data)   
conn.close()  




