import io

def test_upload_text(client):
    file_name = "fake-text-stream.txt"
    data = {
        'image': (io.BytesIO(b"some initial text data"), file_name)
    }
    response = client.post('/upload', data=data)
    assert response.status_code == 200