def create_and_login(client):
    register = {
        "name": "Shelter NGO",
        "email": "shelterngo@example.com",
        "password": "secret123",
        "phone": "8888888888"
    }

    client.post("/api/auth/register", json=register)

    login = client.post("/api/auth/login", json={
        "email": register["email"],
        "password": register["password"]
    })

    return login.json["access_token"]


def test_create_shelter(client):

    token = create_and_login(client)

    payload = {
        "name": "Central Shelter",
        "address": "MG Road",
        "city": "Mumbai",
        "phone": "9999999999",
        "location": {
            "type": "Point",
            "coordinates": [72.8, 19.0]
        },
        "capacity": 50,
        "availableBeds": 20
    }

    res = client.post(
        "/api/shelters",
        json=payload,
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code == 201
