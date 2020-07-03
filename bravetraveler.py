from src.prepare import Prepare
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


@app.post("/api/bravetraveler")
@auth.auth_required
async def bravetraveler(request):
    Prepare(request.json)
    return response.json(
        {'message': 'gotti'},
        headers={'x-served-by': 'bravetraveler'},
        status=200
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, access_log=False, workers=5)
