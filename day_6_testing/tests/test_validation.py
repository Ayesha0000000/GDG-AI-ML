def test_validation(client):
    r = client.get("/secure-data")  # simple test

    assert r.status_code == 401
