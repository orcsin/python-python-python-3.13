import requests

def test_root_call():
    r = requests.get('http://localhost:8080/api/hello', timeout=5)
    assert r.status_code == 200  # nosec


def test_root_call_2():
    r = requests.get('http://localhost:8080/api/hello', timeout=5)
    assert r.status_code != 404  # nosec
