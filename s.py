#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import socket
import sys

HOST = '127.0.0.1'
PORT = 19070   

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

message = sys.argv[1]
s.sendall(message)

recv_msg = s.recv(1024)

s.close()