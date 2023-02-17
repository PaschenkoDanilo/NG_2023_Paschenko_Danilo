from PIL import Image, ImageDraw
from re import findall

with Image.open("newstart.bmp") as img:
    draw = ImageDraw.Draw(img)
    pix = img.load()
    keys = open("keys.txt", "r")

imgMask = 0b00000011
keysList = list([key for key in keys])
indexForRGB = [0, 2, 0, 2]



def decoder():
    text = ""
    index = 0
    while index < len(keysList):
        letter = 0
        key = tuple(map(lambda x: int(x), keysList[index].translate(str.maketrans('', '', ',' '(' ')' '\n')).split(" ")))
        for i in range(0, 4):
            colorCode = pix[key][indexForRGB[i]] & imgMask
            letter <<= 2
            letter |= colorCode
            if i == 1:
                index += 1
                key = tuple(map(lambda x: int(x), keysList[index].translate(str.maketrans('', '', ',' '(' ')' '\n')).split(" ")))
        index += 1
        text += chr(letter)
    print(text)
    keys.close()

decoder()