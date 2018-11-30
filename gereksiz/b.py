#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import socket
from threading import Thread

class myThread(Thread): #Thread class 

    #CONSTRUCTOR FOR THREADS , ASSİGN HOST AND PORT NUMBER.
    def __init__(self, HOST, PORT): 
	    Thread.__init__(self)

	    self.HOST = HOST
	    self.PORT = PORT

    def run(self):
        if self.PORT == 19070 : 
            # THREAD RCV DATA FROM SOURCE USİNG TCP
            self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcp_socket.bind((self.HOST, self.PORT))
            self.tcp_socket.listen(1)
            self.conn,self.addr = self.tcp_socket.accept()
            print 'Client is connected with address: ', self.addr 

        else : 
            #THREAD SEND DATA FROM BROKER TO ROUTERS
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        hello_word(self)

def hello_word(self):

    if(self.PORT == 19070):
        while 1:
            data = self.conn.recv(1024)
            if data:
                print 'received from client',repr(data)
                self.conn.sendall(data)   

    else: 
        while 1:
            self.udp_socket.sendto(data,(self.HOST,self.PORT))




if __name__ == '__main__': 

    Thread_RCV_TCP = myThread('127.0.0.1', 19070)
    
    Thread_SEND_UDP = myThread('127.0.0.1', 19071)

# Start running the threads
	
    Thread_RCV_TCP.start()
    Thread_SEND_UDP.start()

    Thread_RCV_TCP.join()
    Thread_SEND_UDP.join()

# Wait for the threads to finish


