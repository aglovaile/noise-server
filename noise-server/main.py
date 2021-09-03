# FastAPI server for Noise-Server
# By Aglovaile

from fastapi import FastAPI, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, StreamingResponse, FileResponse
from io import BytesIO
import re
import os, random
import cProfile, pstats

from .api.makeNoise import makeNoise
from .api.makeImg import makeImg

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
async def getNoiseJSON(dimensions:str, octaves:int=1, persistence:float=0.5, lacunarity:float=2.0, repeat:int=1024, repeatx:int=1024, repeaty:int=1024, base:int=0):
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
        profiler = cProfile.Profile()
        profiler.enable()
        res = makeNoise(noiseReq)
        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats('cumtime')
        stats.print_stats()

        return res

@app.get(
    '/api/png/random',
    responses= {200: {"content": {'image/png': {}}}},
    response_class=Response
)
async def getRandomImg():
    randomImg = random.choice(os.listdir('./noise-server/static'))   
    imgPath = f'./noise-server/static/{randomImg}'
    return FileResponse(imgPath)


@app.get('/api/png/{dimensions}', responses={200: {'content': {'image/png': {}}}}, response_class=Response)
async def getNoiseImg(
    dimensions:str, 
    octaves:int=1, 
    persistence:float=0.5, 
    lacunarity:float=2.0, 
    base:int=0, 
    frequency:float=1.0,
    maxcolor:str='ffffff',
    mincolor:str='000000',
    grayscale:bool=False
    ):
    profiler = cProfile.Profile()
    profiler.enable()

    img = makeImg(dimensions, octaves, persistence, lacunarity, base, frequency, mincolor, maxcolor, grayscale)
    imgBytes = BytesIO()
    
    img.save(imgBytes, format='PNG')
    imgBytes.seek(0)

    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats()

    return Response(content=imgBytes.read(), media_type='image/png')
