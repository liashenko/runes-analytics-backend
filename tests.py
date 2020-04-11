from app import app
with app.test_client() as client:
    response = client.get('/ping')
    assert response.data == b'OK'
    assert response.status_code == 200