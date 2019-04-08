import pytest
from datetime import date
from app import today

def test_today():
    body, status, _ = today()
    assert status == 200
    assert body == '{"today": "%s"}' % date.today()