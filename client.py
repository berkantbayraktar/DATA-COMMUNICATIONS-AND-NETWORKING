#echo client program
import socket

HOST = '127.0.0.1'
PORT = 50007

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while 1:
    inp = raw_input("")
    s.sendall(inp)
    data = s.recv(1024)
    print 'received back from server',repr(data)
s.close()

