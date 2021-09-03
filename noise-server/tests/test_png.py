from fastapi.testclient import TestClient
from PIL import Image
from io import BytesIO
from main import app

client = TestClient(app)

def test_png():
    x = 20
    y = 30
    res = client.get(f'/api/png/{x}x{y}')
    with Image.open(BytesIO(res.content)) as img:
        assert res.status_code == 200
        assert res.headers['content-type'] == 'image/png'
        assert img.size[0] == x and img.size[1] == y