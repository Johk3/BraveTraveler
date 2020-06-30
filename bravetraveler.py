from src.prepare import Prepare
import sanic

class BraveTraveler:
    """Monitoring service for incoming data"""
    def fetchData(self):
        return 1

if __name__ == "__main__":
    BraveTraveler = BraveTraveler()
    data = BraveTraveler.fetchData()

    Fetch = Prepare(data)
