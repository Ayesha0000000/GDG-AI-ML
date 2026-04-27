def test_config(client):
    r = client.get("/config")
    data = r.json()

    assert r.status_code == 200
    assert "app_name" in data
    assert "api_key" not in data
