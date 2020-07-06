from src.log import *

import json

# Local UNIX socket requirements
import socket


class Transmitter:
    """INSERT TEXT"""
    def __init__(self):
        # Create socket
        self.server_address = "./.ipc_socket"
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        # Connect socket
        LOG_INFO(f"Connecting to {self.server_address}")
        try:
            self.sock.connect(self.server_address)
        except socket.error as e:
            LOG_FAIL(f"Could not connect to socket: {e}")
            exit(1)


    def parse_and_send(self, data):
        data = self.parse(data)
        self.send(data)


    def parse(self, data):
        """Parse the data to work with frontend"""
        for key, value in data.items():
            LOG_INFO(f"Parsing {key}:{value}")
        return data


    def send(self, data):
        """Send data to frontend over local socket"""
        LOG_INFO(f"Sending data over IPC")
        self.sock.sendall("asd".encode())
