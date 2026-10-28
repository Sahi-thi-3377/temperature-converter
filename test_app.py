import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['version'] == "1.0.0"

def test_celsius_to_fahrenheit_success(client):
    response = client.post('/convert/celsius-to-fahrenheit', json={"celsius": 0})
    assert response.status_code == 200
    assert response.get_json()['output_fahrenheit'] == 32.0

    response = client.post('/convert/celsius-to-fahrenheit', json={"celsius": 100})
    assert response.status_code == 200
    assert response.get_json()['output_fahrenheit'] == 212.0

def test_celsius_to_fahrenheit_invalid_input(client):
    response = client.post('/convert/celsius-to-fahrenheit', json={"celsius": "invalid_string"})
    assert response.status_code == 400
    assert "error" in response.get_json()
