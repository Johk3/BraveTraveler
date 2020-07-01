from src.prepare import Prepare
from sanic import Sanic
from sanic import response
from sanic.response import json
from sanic.views import HTTPMethodView
from sanic_cors import CORS, cross_origin

# --- DEV nodemon stuff
import os
import atexit
def exit_handler():
    os.system("pkill python")
atexit.register(exit_handler)
# --- DEV nodemon stuff

app = Sanic(__name__)
CORS(app)

class BraveTraveler(HTTPMethodView):
    """Monitoring service for incoming data"""
    async def get(self, request):
        return 202
    async def post(self, request):
        Prepare(request.json)
        return response.json(
        {'message': 'Gotti'},
        headers={'X-Served-By': 'sanic'},
        status=200
    )

app.add_route(BraveTraveler.as_view(), "/api/bravetraveler")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, access_log=False, workers=5)
