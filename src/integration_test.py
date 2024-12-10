from werkzeug.datastructures import FileStorage

def test_upload_database_chat(client):

    file = FileStorage(
        stream = open("OpenAIsSuccess.txt", "rb"),
        filename = "OpenAIsSuccess.txt",
        content_type = "text/plain",
    )

    # Test uploading private data file
    response = client.post(
        "/upload",
        data = dict(file = file)
    )

    assert response.status_code == 200

    # Test chat withprivate data with Gemini
    response = client.post('/', data = {"promt": "what is openai"})
    assert response.status_code == 400