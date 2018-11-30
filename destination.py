#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import socket
from threading import Thread
import time
import json

class myThread(Thread): #Thread class 

    #CONSTRUCTOR FOR THREADS , ASSİGN HOST AND PORT NUMBER.
    def __init__(self, HOST, PORT): 
	    Thread.__init__(self)

	    self.HOST = HOST
	    self.PORT = PORT
    
    def run(self):
        if(self.PORT == 25572):  # r1
            self.r1_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.r1_udp_sock.bind(('10.10.3.2', self.PORT))

            while 1:
                self.data,self.addr = self.r1_udp_sock.recvfrom(1024)
                if self.data:
 
                    self.dest_received_time = json.loads(self.data)['timestamp'] # timestamp of the message
                    self.message = json.loads(self.data)['message'] # actual message from the server
                    #print("Sent at :{}".format(str(time.time())))
                    #print("Received at destination at:{}".format(self.dest_received_time))
                    print(self.message)
                 
                    
        else:   #r2
   
            self.r2_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.r2_udp_sock.bind(('10.10.3.2', self.PORT))
            while 1:
                self.data,self.addr = self.r2_udp_sock.recvfrom(1024)
                if self.data:
                   
                    self.dest_received_time = json.loads(self.data)['timestamp'] # timestamp of the message
                    self.message = json.loads(self.data)['message'] # actual message from the server
                    #print("Sent at :{}".format(str(time.time())))
                    #print("Received at destination at:{}".format(self.dest_received_time))
                    print(self.message)
        
                    




if __name__ == '__main__': 

    Thread_r1 = myThread('10.10.2.2', 25572)
    
    Thread_r2 = myThread('10.10.4.2', 25573)

# Start running the threads
	
    Thread_r1.start()
    Thread_r2.start()

    Thread_r1.join()
    Thread_r2.join()
