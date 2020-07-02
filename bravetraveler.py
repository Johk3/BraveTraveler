from src.data_transmitter import Transmitter
from src.log import *
from sanic import Sanic
from sanic import response
from sanic.response import json
from sanic.views import HTTPMethodView
from sanic_cors import CORS, cross_origin

app = Sanic(__name__)
CORS(app)

LOG_INFO("Creating IPC transmitter")

transmitter = Transmitter()

class BraveTraveler(HTTPMethodView):
    """Monitoring service for incoming data"""
    # Respond to GET requests
    async def get(self, request):
        return 202


    # Respond to POST requests
    async def post(self, request):
        # Parse and send data
        transmitter.parse_and_send(request.json)

        return response.json(
        {'message': 'Gotti'},
        headers={'X-Served-By': 'sanic'},
        status=200
    )

app.add_route(BraveTraveler.as_view(), "/api/bravetraveler")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, access_log=False, workers=5)
