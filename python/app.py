from flask import Flask, jsonify
from flask_cors import CORS
from datetime import date
import requests
import re


app = Flask(__name__)
CORS(app)

URL = "https://www.thinkful.com/api/advisors/availability"

r = requests.get(url = URL)
data = r.json()
this_weeks_dates = list(data.keys())
sorted_dates = sorted(this_weeks_dates, key=lambda x: int(re.search(r'\d+$', x).group()))

@app.route("/today", methods=["GET"])
def today():
    return jsonify({"today": sorted_dates[0]})

@app.route("/tomorrow", methods=["GET"])
def tomorrow():
    return jsonify({"tomorrow": sorted_dates[1]})

@app.route("/two_days_from_today", methods=["GET"])
def two_days_from_today():
    return jsonify({"two_days_from_today": sorted_dates[2]})

@app.route("/three_days_from_today", methods=["GET"])
def three_days_from_today():
    return jsonify({"three_days_from_today": sorted_dates[3]})


@app.route("/four_days_from_today", methods=["GET"])
def four_days_from_today():
    return jsonify({"four_days_from_today": sorted_dates[4]})

@app.route("/five_days_from_today", methods=["GET"])
def five_days_from_today():
    return jsonify({"five_days_from_today": sorted_dates[5]})

@app.route("/six_days_from_today", methods=["GET"])
def six_days_from_today():
    return jsonify({"six_days_from_today": sorted_dates[6]})