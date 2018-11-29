#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import socket
import sys

HOST = '127.0.0.1'
PORT = 19070   

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

while 1:
    message = raw_input('message: ')
    if message:
        s.send(message)

s.close()