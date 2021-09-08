from fastapi.testclient import TestClient
import json
from main import app

client = TestClient(app)

def test_1d_noise():
    x = 20
    res = client.get(f'/api/noise/{x}')
    noiseJson = res.json()

    assert res.status_code == 200
    assert res.headers['content-type'] == 'application/json'
    assert noiseJson['dimensions'][0] == x
    assert len(noiseJson['data']) > 0
    assert checkNoiseList(noiseJson['data'])


def test_2d_noise(): 
    x= 20
    y = 30
    res = client.get(f'/api/noise/{x}x{y}')
    noiseJson = res.json()
    data = noiseJson['data']

    assert res.status_code == 200
    assert res.headers['content-type'] == 'application/json'
    assert len(data) > 0
    assert checkNoiseList(data)


def test_3d_noise(): 
    x= 15
    y = 20
    z = 10
    res = client.get(f'/api/noise/{x}x{y}x{z}')
    noiseJson = res.json()
    data = noiseJson['data']

    assert res.status_code == 200
    assert res.headers['content-type'] == 'application/json'
    assert len(data) > 0
    assert checkNoiseList(data)

def test_4d_noise(): 
    x= 15
    y = 20
    z = 10
    w = 5
    res = client.get(f'/api/noise/{x}x{y}x{z}x{w}')
    noiseJson = res.json()
    data = noiseJson['data']

    assert res.status_code == 200
    assert res.headers['content-type'] == 'application/json'
    assert len(data) > 0
    assert checkNoiseList(data)


def checkNoiseList(arr):
    # Check recursively that all values are between -1 and 1
    for i in arr:
        if not type(i) == list:
            if not -1 <= i <= 1:
                return False
        else:
            if not checkNoiseList(i):
                return False
    return True