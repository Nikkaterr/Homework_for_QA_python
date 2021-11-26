import requests
import pytest


def test_valid_status_code_check(check_url, status_code):
    res = requests.get(check_url)
    assert res.status_code == status_code
