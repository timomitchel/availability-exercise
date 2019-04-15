import code
from flask import Flask, jsonify
from flask_cors import CORS
from datetime import date

import requests
import re

app = Flask(__name__)
CORS(app)

def make_request():
    URL = "https://www.thinkful.com/api/advisors/availability"
    return requests.get(url = URL)

data = make_request().json()
this_weeks_dates = list(data.keys())
sorted_dates = sorted(this_weeks_dates, key=lambda x: int(re.search(r'\d+$', x).group()))

def sort_by_id(sorted_dates):
    sorted_by_id = {}
    for val in sorted_dates:
        for key, value in sorted(data[val].items()):
            sorted_by_id.setdefault(value, []).append(key)
    return sorted_by_id


@app.route("/available_times", methods=["GET"])
def available_times():
    return jsonify({"available_times": sort_by_id(sorted_dates)})
