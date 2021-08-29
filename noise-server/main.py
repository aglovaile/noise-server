# FastAPI server for Noise-Server
# By Aglovaile

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import Optional
import re

from makenoise import makenoise as makeNoise

# def makeNoise(req):
#     return req

app = FastAPI()

# Home request
@app.get('/')
async def getHome():
    return 'We will make it noisy.'

# Return a grayscale image with pixels requestee
@app.get('/img/{x}x{y}')
async def getImg(x: int, y: int):
    return f'You will get an image of {x}x{y}'

@app.get('/api/noise/{dimensions}/')
async def getNoiseJSON(dimensions:str, octaves:int=1, persistence:float=0.5, lacunarity:float=2.0, repeat:int=1024, repeatx:int=1024, repeaty:int=1024, repeatz=None, base:int=0):
    if not re.search('(\d+)', dimensions):
        res = jsonable_encoder({'error': "Invalid dimensions for Perlin noise."})
        return JSONResponse(res)
    else:
        noiseReq = {
            'dimensions': list(map(lambda i: int(i), re.findall('\d+', dimensions))),   # Convert XxYxZxW str format into List of integers
            'octaves': octaves,
            'persistence': persistence,
            'lacunarity': lacunarity,
            'repeat': repeat,
            'repeatx': repeatx,
            'repeaty': repeaty,
            'base': base
        }
        res = jsonable_encoder(makeNoise(noiseReq))
        return JSONResponse(res)

    return dimension