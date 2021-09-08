import re
from PIL import Image 
import numpy
from noise import pnoise2, snoise2
from .makeNoise import twoDnoise


def makeImg(req):
    grayscale = req['grayscale']
    mincolor = req['mincolor']
    maxcolor = req['maxcolor']
    dimensions = req['dimensions']

    if len(dimensions) < 2:
        dimensions.append(dimensions[0])

    noiseList = twoDnoise(req)
    midColor = 128 if grayscale else int(maxcolor, 16) - int(mincolor, 16)

    pixelsList = []
    for yRow in noiseList['data']:
        row = []
        for x in yRow:

            pixelNoise = round((x * (midColor - 1)) + midColor)

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
   
    return newPng


if __name__ == '__main__':
    makeImg