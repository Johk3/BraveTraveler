class Prepare:
    """INSERT TEXT"""
    def __init__(self, data):
        self.data = data
        self.parse()

    def parse(self):
        """Parse the data to work with frontend"""
        LOG_INFO(self.data)
