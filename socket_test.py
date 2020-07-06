# Testing server to test IPC

import socket
import sys
import os

from src.log import *

server_address = './.ipc_socket'

# Make sure the socket does not already exist
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        LOG_FAIL("Socket path in use, unable to unlink")
        exit(1)

# Create a socket
LOG_INFO("Creating socket")
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Bind the socket to the port
LOG_INFO(f"Starting server at {server_address}")
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    LOG_INFO("Waiting for connections")
    conn, addr = sock.accept()
    try:
        LOG_INFO("New connection established")
        # Receive the data in small chunks and print it
        while True:
            data = conn.recv(1024)
            print(data)
            if data:
                LOG_INFO(f"Received {data}")
            else:
                LOG_WARN("Client lost")
                break
            
    finally:
        # Clean up the connection
        LOG_INFO("Cleaning up")
        conn.close()

