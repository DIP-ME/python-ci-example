import pytest

from app.web import create_app


@pytest.fixture()
def client():
    return create_app().test_client()


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_add_route(client):
    resp = client.get("/add?a=2&b=3")
    assert resp.status_code == 200
    assert resp.get_json()["result"] == 5


def test_divide_by_zero_route(client):
    resp = client.get("/divide?a=1&b=0")
    assert resp.status_code == 400
