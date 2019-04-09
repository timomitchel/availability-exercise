from flask import Flask, jsonify
from flask_cors import CORS
from datetime import date
import requests


app = Flask(__name__)
CORS(app)


@app.route("/today", methods=["GET"])
def today():
    return jsonify({"today": date.today().isoformat()})
