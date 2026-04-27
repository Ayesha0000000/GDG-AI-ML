def test_secure_fail(client):
    r = client.get("/secure-data")
    assert r.status_code == 401


def test_secure_success(client):
    r = client.get("/secure-data", headers={"X-API-Key": "test-key"})
    assert r.status_code == 200
