from flask import Flask, json
from flask_cors import CORS
from datetime import date
import requests

app = Flask(__name__)
CORS(app)


@app.route("/today", methods=["GET"])
def today():
    return _json_response({"today": str(date.today())})


def _json_response(payload, status=200):
    return json.dumps(payload), status, {'content-type': 'application/json'}