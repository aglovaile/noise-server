import re
import png
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

xDim = 1280
yDim = 720

octaves = 1
freq = .001
persistence = 100.5
base = 0
repeatx = None
repeaty = None
offset = 0

colorRange = int('0f000', 16)

pixelsList = []

for y in range(yDim):
    row = []
    for x in range(xDim):
        # Pixel val is three vals 0-255
        # Convert max hex color space into num, multiply by noise val, round to nearest int
        pixelNoise = round((snoise2(x * freq, y * freq, octaves, persistence, base) * colorRange / 2) + ((colorRange + 1) / 2))
        noiseHex = hex(pixelNoise).replace('0x', '').zfill(6)
        rgbList = re.findall('..', noiseHex)
        # print(noiseHex, rgbList)

        for i in list(rgbList):
            row.append(int(i, 16))
    pixelsList.append(row)
png.from_array(pixelsList, 'RGB').save(f'{randrange(999999)}.png')