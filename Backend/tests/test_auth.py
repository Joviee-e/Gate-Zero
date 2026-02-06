def test_register_and_login(client):

    payload = {
        "name": "Test NGO",
        "email": "testngo@example.com",
        "password": "secret123",
        "phone": "9999999999"
    }

    # Register
    res = client.post("/api/auth/register", json=payload)
    assert res.status_code in [201, 400]

    # Login
    login_res = client.post("/api/auth/login", json={
        "email": payload["email"],
        "password": payload["password"]
    })

    assert login_res.status_code == 200
    assert "access_token" in login_res.json
