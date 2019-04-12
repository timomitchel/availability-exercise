import datetime
from app import app


def test_today():
    with app.test_client() as cli:
        resp = cli.get('/today')
        assert resp.status_code == 200
        assert resp.json == {"today": "{}".format(datetime.date.today())}


def test_tomorrow():
    with app.test_client() as cli:
        resp = cli.get('/tomorrow')
        assert resp.status_code == 200
        assert resp.json == {
            "tomorrow":
            "{}".format(datetime.date.today() + datetime.timedelta(days=1))
        }


def test_two_days_from_today():
    with app.test_client() as cli:
        resp = cli.get('/two_days_from_today')
        assert resp.status_code == 200
        assert resp.json == {
            "two_days_from_today":
            "{}".format(datetime.date.today() + datetime.timedelta(days=2))
        }


def test_three_days_from_today():
    with app.test_client() as cli:
        resp = cli.get('/three_days_from_today')
        assert resp.status_code == 200
        assert resp.json == {
            "three_days_from_today":
            "{}".format(datetime.date.today() + datetime.timedelta(days=3))
        }


def test_four_days_from_today():
    with app.test_client() as cli:
        resp = cli.get('/four_days_from_today')
        assert resp.status_code == 200
        assert resp.json == {
            "four_days_from_today":
            "{}".format(datetime.date.today() + datetime.timedelta(days=4))
        }


def test_five_days_from_today():
    with app.test_client() as cli:
        resp = cli.get('/five_days_from_today')
        assert resp.status_code == 200
        assert resp.json == {
            "five_days_from_today":
            "{}".format(datetime.date.today() + datetime.timedelta(days=5))
        }


def test_six_days_from_today():
    with app.test_client() as cli:
        resp = cli.get('/six_days_from_today')
        assert resp.status_code == 200
        assert resp.json == {
            "six_days_from_today":
            "{}".format(datetime.date.today() + datetime.timedelta(days=6))
        }