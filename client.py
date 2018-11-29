import socket
import json
import time

HOST, PORT = "localhost", 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = raw_input("Send:")
    sent_time = float(time.time())
    sock.sendto(data + "\n", (HOST, PORT))
    received = sock.recv(1024)
    dest_received_time = json.loads(received)['timestamp'] # timestamp of the message
    message = json.loads(received)['message'] # actual message from the server
    print("Sent at :{}".format(sent_time))
    print("Received at destination at:{}".format(dest_received_time))
    #print("End-to-end delay : " + str(dest_received_time - sent_time) + " ms")
