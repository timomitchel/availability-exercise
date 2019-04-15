import datetime
from app import app


def test_available_times():
    with app.test_client() as cli:
        resp = cli.get('/available_times')
        assert resp.status_code == 200
        assert resp.json['available_times']
