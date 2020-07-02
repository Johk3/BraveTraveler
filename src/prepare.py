from src.log import *

# Local UNIX socket requirements
import socket


class Prepare:
    """INSERT TEXT"""
    def __init__(self, data):
        self.data = data

        # Create socket
        self.server_address = "./.ipc_socket"
        self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        # Connect socket
        LOG_INFO(f"Connecting to {self.server_address}")
        try:
            sock.connect(self.server_address)
        except:
            LOG_FAIL("Could not connect to socket")
            exit(1)

        self.parse()


    def parse(self):
        """Parse the data to work with frontend"""
        for key, value in self.data.items():
            LOG_INFO(value)


    def send(self):
        """Send data to frontend over local socket"""
        self.socket.sendall(json.dumps(self.data).encode("UTF-8"))
