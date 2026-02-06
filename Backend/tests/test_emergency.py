def test_emergency_requires_coords(client):

    res = client.get("/api/emergency")

    assert res.status_code == 400
