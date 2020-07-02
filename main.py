import socket
import sys
import os
import threading


server_address = './.ipc_socket'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

print(f"Connecting to {server_address}")
try:
    sock.connect(server_address)
except:
    print(f"Failed")
    exit(1)


def sender():
    while True:
        i = str(input())
        sock.sendall(i.encode("UTF-8"))

def receiver():
    while True:
        print(sock.recv(1024))

threading.Thread(target=sender).start()
threading.Thread(target=receiver).start()
