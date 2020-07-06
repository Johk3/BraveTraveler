from src.data_transmitter import Transmitter
from src.log import *
from sanic import Sanic
from sanic import response
from sanic.response import json
from sanic.views import HTTPMethodView
from sanic_cors import CORS, cross_origin
from sanic_token_auth import SanicTokenAuth

app = Sanic(__name__)
key = open("key", "r")
auth = SanicTokenAuth(app, secret_key=key.read().strip(),
                      header="X-Brave-Traveler-Auth-Token")
CORS(app)

LOG_INFO("Creating IPC transmitter")
transmitter = Transmitter()


@app.post("/api/bravetraveler")
@auth.auth_required
async def bravetraveler(request):
    transmitter.parse_and_send(request.json)
    return response.json(
        {'message': 'gotti'},
        headers={'x-served-by': 'bravetraveler'},
        status=200
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, access_log=False, workers=5)
