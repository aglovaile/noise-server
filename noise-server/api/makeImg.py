import re
import png
# from PIL import Image
from random import randrange
from noise import pnoise2, snoise2

# if len(sys.argv) not in (2,3) or '--help' in sys.argv or '-h' in sys.argv:
#     print('2dtexture.py FILE [OCTAVES]')
#     print()
#     print(__doc__)

#     raise SystemExit

# f = open(sys.argv[1], 'wt')

# if len(sys.argv) > 2:
#     octaves = int(sys.argv[1])
# else:
#     octaves = 1

# freq = 16.0 * octaves

# f.write('P2\n')
# f.write('256 256\n')
# f.write('255\n')

# # Add pixels for each row column of x, each row of y
# for y in range(256):
#     for x in range (256):
#         # moise integer is -1 < x < 1
#         # middle point is 128
#         pixel = int(snoise2(x / freq, y / freq, octaves) * 127) + 128
#         f.write(f'{pixel}\n')
# f.close()

def makeImg(dimensions, octaves, persistence, lacunarity, base, frequency):
    xy = re.findall('\d+', dimensions)

    xDim = int(xy[0])
    yDim = int(xy[1])

    colorRange = int('0f000', 16)

    pixelsList = []

    for y in range(yDim):
        row = []
        for x in range(xDim):
            # Pixel val is three vals 0-255
            # Convert max hex color space into num, multiply by noise val, round to nearest int
            pixelNoise = round((snoise2(x * frequency, y * frequency, octaves, persistence, base) * colorRange / 2) + ((colorRange + 1) / 2))
            noiseHex = hex(pixelNoise).replace('0x', '').zfill(6)
            rgbList = re.findall('..', noiseHex)
            # print(noiseHex, rgbList)

            for i in list(rgbList):
                row.append(int(i, 16))
        pixelsList.append(row)
    # return pixelsList
    return png.from_array(pixelsList, 'RGB')

if __name__ == '__main__':
    makeImg