from log import *

class Prepare:
    """INSERT TEXT"""
    def __init__(self, data):
        self.data = data
        self.parse()

    def parse(self):
        """Parse the data to work with frontend"""
        for key, value in self.data.items():
            LOG_INFO(value)
