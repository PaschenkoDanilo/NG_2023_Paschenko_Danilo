from PIL import Image, ImageDraw
from random import randint

with Image.open("start.bmp") as img:
    draw = ImageDraw.Draw(img)
    pix = img.load()
    width = img.size[0]
    height = img.size[1]
    keys = open("keys.txt", "w+")

text = "rol kek LOL kekich rofls KEKWait"



imgMask = 0b11111100
textMask = 0b11000000
indexForRGB = [0, 2, 0, 2]

def encoder():
    index = 0
    while index < len(text):
        letter = ord(text[index])
        key = randint(0, width - 10), randint(0, height - 10)
        for i in range(0, 4):
            colorCode = pix[key][indexForRGB[i]] & imgMask
            letterMask = letter & textMask
            letterMask >>= 6
            colorCode |= letterMask
            encodeInImage(colorCode, key, i)
            letter <<= 2
            if i == 1:
                key = randint(0, width - 10), randint(0, height - 10)
        index += 1
    img.save("newstart.bmp", "BMP")
    keys.close()

def encodeInImage(colorCode, key, index):
    if index == 0 or index == 2:
        draw.point(key, (colorCode, pix[key][1], pix[key][2]))
    elif index == 1 or index == 3:
        draw.point(key, (pix[key][0], pix[key][1], colorCode))
    if index == 1 or index == 3:
        keys.write(str(key) + "\n")

encoder()