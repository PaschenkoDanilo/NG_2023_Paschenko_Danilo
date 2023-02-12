from PIL import Image, ImageDraw
from random import randint

img = Image.open("start.bmp")
draw = ImageDraw.Draw(img)
pix = img.load()

width = img.size[0]
heigth = img.size[1]

keys = open("keys.txt", "w+")


text = "rol kek LOL kekich rofls KEKWait, LMAOfdjfgjlgfojdfhjdfhjhhjhdfgjldlgjkdfghldkfjglsfghfhfghdhdfufgufuhguhfguhfuhfghfuhghfghfghkdf;strhhrt74545477shugrhb "
imgMask = 0b11111100
textMask = 0b11000000


def encoder():
    for symbol in text:
        letter = ord(symbol)
        encodeFirstHalf(letter)
        encodeSecondHalf(letter)
    img.save("newstart.bmp", "BMP")
    keys.close()

def encodeFirstHalf(letter):
    key = randint(0, width - 10),randint(0, heigth - 10)
    red = pix[key][0] & imgMask
    letterMask = letter & textMask
    letterMask >>= 6
    red |= letterMask
    letter <<= 2

    blue = pix[key][2] & imgMask
    letterMask = letter & textMask
    letterMask >>= 6
    blue |= letterMask
    encodeInFile(key, red, blue)

def encodeSecondHalf(letter):
    key = randint(0, width - 10),randint(0, heigth - 10)
    red = pix[key][0] & imgMask
    letter <<= 4
    letterMask = letter & textMask
    letterMask >>= 6
    red |= letterMask
    letter <<= 2

    blue = pix[key][2] & imgMask
    letterMask = letter & textMask
    letterMask >>= 6
    blue |= letterMask
    encodeInFile(key, red, blue)

def encodeInFile(key, red, blue):
    green = pix[key][1]
    draw.point(key, (red, green, blue))
    keys.write(str(key) + "\n")

    
encoder()