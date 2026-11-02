from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Welcome to DevOps Application - Production and Development!"


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

def test_contact():
    client = app.test_client()
    response = client.get("/contact")
    assert response.status_code == 200
    assert response.json == {
        "email": "joelpaul@gmail.com",
        "team": "DevOps Team"
    }

def test_status():
    client = app.test_client()
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json == {
        "application": "running",
        "environment": "development"
    }
