#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import socket
from threading import Thread
import time
import json

class myThread(Thread): # Thread class 

    #constructor for thread , construct with host and port number
    def __init__(self, HOST, PORT): 
	    Thread.__init__(self)
	    self.HOST = HOST
	    self.PORT = PORT
    
    def run(self):
        if(self.PORT == 25572):  # if port number reserved for router1
            # create and bind socket for receiving data from router1
            self.r1_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.r1_udp_sock.bind((self.HOST, self.PORT))

            while 1:
                # receive 1024 byte data from router1
                self.data,self.addr = self.r1_udp_sock.recvfrom(1024)
                # if received data is valid
                if self.data:
                    self.src_send_time = json.loads(self.data)['timestamp'] # timestamp of the message at source
                    self.message = json.loads(self.data)['message'] # actual message from the source
                    # print time difference i.e. end-to-end delay
                    print('end-to-end delay:',time.time() -  float(self.src_send_time) )
                 
                    
        else:   #if port number reserved for router2
            # create and bind socket for receiving data from router2
            self.r2_udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.r2_udp_sock.bind((self.HOST, self.PORT))
            while 1:
                # receive 1024 byte data from router2
                self.data,self.addr = self.r2_udp_sock.recvfrom(1024)
                # if received data is valid
                if self.data:  
                    self.src_send_time = json.loads(self.data)['timestamp'] # imestamp of the message at source
                    self.message = json.loads(self.data)['message'] # actual message from the source
                    # print time difference i.e. end-to-end delay
                    print('end-to-end delay:',time.time() - float(self.src_send_time) )
        
                    




if __name__ == '__main__': 

    # create thread for router1 socket
    Thread_r1 = myThread('10.10.3.2', 25572)
    
    # create thread for router2 socket
    Thread_r2 = myThread('10.10.3.2', 25573)

# Start running the threads
	
    Thread_r1.start()
    Thread_r2.start()

# Close threads
    Thread_r1.join()
    Thread_r2.join()
