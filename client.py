#echo client program
import socket

HOST = '127.0.0.1'
PORT = 50007

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

inp = raw_input("yaz icinden gecenleri be baba \n")
s.sendall(inp)
data = s.recv(1024)
print 'received from server',repr(data)
s.close()

