def test_main_get_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_main_post_route(client):
    response = client.post('/', data = {"promt": "what is openai"})
    assert response.status_code == 400

def test_upload_post_route(client):
    response = client.post('/upload', data = {"promt": "what is openai"})
    assert response.status_code == 200
