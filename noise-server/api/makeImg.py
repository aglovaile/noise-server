import re
# import png
from PIL import Image, ImageOps
import numpy
from random import randrange
from noise import pnoise2, snoise2
import cProfile, pstats

def makeImg(dimensions, octaves, persistence, lacunarity, base, frequency, mincolor, maxcolor, grayscale):
    profiler = cProfile.Profile()
    profiler.enable()

    xy = re.findall('\d+', dimensions)

    xDim = int(xy[0])
    yDim = int(xy[1])

    midColor = 128 if grayscale else int(maxcolor, 16) - int(mincolor, 16)

    pixelsList = []

    for y in range(yDim):
        row = []
        for x in range(xDim):
            # Pixel val is three vals 0-255
            # Convert max hex color space into num, multiply by noise val, round to nearest int
            pixelNoise = round((pnoise2(x * frequency, y * frequency, octaves=octaves, lacunarity=lacunarity, persistence=persistence, base=base) * (midColor - 1)) + midColor)
            
            if grayscale:
                noiseHex = hex(pixelNoise)[2:]
                rgbList = [noiseHex, noiseHex, noiseHex]
            else:
                noiseHex = hex(pixelNoise)[2:].zfill(6)
                rgbList = [noiseHex[0:2], noiseHex[2:4], noiseHex[4:]]

            row.append([int(rgbList[0], 16), int(rgbList[1], 16), int(rgbList[2], 16)])
        pixelsList.append(row)
    pixelsArray = numpy.array(pixelsList, dtype=numpy.uint8)
    newPng = Image.fromarray(pixelsArray, mode='RGB')

    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats()
    
    return newPng

if __name__ == '__main__':
    makeImg