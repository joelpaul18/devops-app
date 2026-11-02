from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Welcome to DevOps Application!"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "UP"}

def test_about():
    client = app.test_client()
    response = client.get("/about")
    assert response.status_code == 200
    assert b"DevOps practical lab" in response.data

def test_version():
    client = app.test_client()
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json == {"version": "1.0.0"}
