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
        if(self.PORT == 19073):  # r1

            self.r1_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.r1_udp_sock.bind((self.HOST, self.PORT))

            while 1:
                self.data,self.addr = self.r1_udp_sock.recvfrom(1024)
                if self.data:
                    print 'destination got the message from r1 ' ,repr(self.data)

        else:   #r2

            self.r2_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.r2_udp_sock.bind((self.HOST, self.PORT))
            while 1:
                self.data,self.addr = self.r2_udp_sock.recvfrom(1024)
                if self.data:
                    print 'destination got the message from r2 ' ,repr(self.data)





if __name__ == '__main__': 

    Thread_r1 = myThread('127.0.0.1', 19073)
    
    Thread_r2 = myThread('127.0.0.1', 19074)

# Start running the threads
	
    Thread_r1.start()
    Thread_r2.start()

    Thread_r1.join()
    Thread_r2.join()