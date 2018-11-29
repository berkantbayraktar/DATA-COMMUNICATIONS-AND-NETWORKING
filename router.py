#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from threading import Thread

class receiver(Thread): #Thread class

    #CONSTRUCTOR FOR THREADS , ASSIGN HOST AND PORT NUMBER.
    def __init__(self, HOST, PORT):
	    Thread.__init__(self)
	    self.HOST = HOST
	    self.PORT = PORT
    def run(self):
            # receive data from broker
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.bind((self.HOST, self.PORT))
            print 'Receives from: ', self.addr
            while True:
                data = self.socket.recvfrom(1024)
                if data:
                    print 'Received from broker :',repr(data)
                    #send to destination
                    self.socket.sendall(data)
                    print "Send to destination : " , repr(data)


if __name__ == '__main__':

    recv_thread = receiver('127.0.0.1', 19070)

# Start running the threads
recv_thread.start()
send_thread.start()

recv_thread.join()
send_thread.join()


# Wait for the threads to finish
