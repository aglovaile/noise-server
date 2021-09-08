from fastapi.testclient import TestClient
import json
from main import app

client = TestClient(app)

def test_1d_noise():
    x = 20
    res = client.get(f'/api/noise/{x}')
    assert res.status_code == 200
    assert res.headers['content-type'] == 'application/json'
    # with json.loads(res.content) as noiseJson:

def test_2d_noise(): 
    x= 20
    y = 30
    res = client.get(f'/api/noise/{x}x{y}')

    assert res.status_code == 200
    assert res.headers['content-type'] == 'application/json'