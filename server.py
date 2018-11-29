#echo server program
import socket

HOST = '' # IPv4 Address of Server
PORT = 50007  # PORT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
s.bind((HOST, PORT))
s.listen(1)
conn,addr = s.accept()
print 'Client is connected with address: ',addr 
while 1:
    data = conn.recv(1024)
    if not data: 
        break
    conn.sendall(data)   
conn.close()  




