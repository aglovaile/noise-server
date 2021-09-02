from noise import pnoise1, snoise2, snoise3, snoise4
import re

# Main function takes a req dict from the API and returns a dict of noise lists


def makeNoise(req):
    dimensions = req['dimensions']
    try:
        noiseType = {
            0: oneDnoise,
            1: twoDnoise,
            2: threeDnoise,
            3: fourDnoise
        }[len(dimensions) - 1]
        return noiseType(req)
    except RuntimeError as err:
        error = {'error': 'Incorrect request for Perlin noise'}
        req['error'] = error
        print(err)
        return req


def oneDnoise(req):
    dimensions = req['dimensions']
    octaves = req['octaves']
    persistence = req['persistence']
    lacunarity = req['lacunarity']
    repeat = req['repeat']
    base = req['base']

    xList = []

    for x in range(dimensions[0]):
        xList.append(pnoise1(x, octaves))

    res = req
    res['data'] = xList
    del res['repeatx']
    del res['repeaty']

    return res


def twoDnoise(req):
    dimensions = req['dimensions']
    octaves = req['octaves']
    persistence = req['persistence']
    lacunarity = req['lacunarity']
    repeatx = req['repeatx']
    repeaty = req['repeaty']
    base = req['base']

    xyList = []

    for y in range(int(dimensions[1])):
        row = []
        for x in range(int(dimensions[0])):
           row.append(snoise2(x, y, octaves, persistence, lacunarity, repeatx, repeaty, base))
        xyList.append(row)
    
    res = req
    res['data'] = xyList
    del res['repeat']

    return req

def threeDnoise(req):
    dimensions = req['dimensions']
    octaves = req['octaves']
    persistence = req['persistence']
    lacunarity = req['lacunarity']
    base = req['base']

    xyzList = []

    print(dimensions)

    for z in range(dimensions[2]):
        rowY = []
        for y in range(dimensions[1]):
            rowX = []
            for x in range(dimensions[0]):
                print(x,y,z)
                rowX.append(snoise3(x, y, z, octaves, persistence, lacunarity))
        rowY.append(rowX)
        xyzList.append(rowY)
    res = {}
    for i in req:
        if not re.search('repeat', i):
            res[i] = req[i]
    res['data'] = xyzList

    return res

def fourDnoise(req):
    dimensions = req['dimensions']
    octaves = req['octaves']
    persistence = req['persistence']
    lacunarity = req['lacunarity']
    base = req['base']

    xyzwList = []

    for w in range(dimensions[3]):
        rowZ = []
        for z in range(dimensions[2]):
            rowY = []
            for y in range(dimensions[1]):
                rowX = []
                for x in range(dimensions[0]):
                    rowX.append(snoise3(x, y, z, octaves, persistence, lacunarity))
                rowY.append(rowX)
            rowZ.append(rowY)
        xyzwList.append(rowZ)
    res = {}
    for i in req:
        if not re.search('repeat', i):
            res[i] = req[i]
    res['data'] = xyzwList

    return res

if __name__ == '__main__':
    makenoise