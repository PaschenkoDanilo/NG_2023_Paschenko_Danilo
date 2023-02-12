from PIL import Image, ImageDraw
from re import findall

img = Image.open("newstart.bmp")
draw = ImageDraw.Draw(img)
pix = img.load()

keys = open("keys.txt", "r")

imgMask = 0b000000011
keysList = list([key for key in keys])



def decoder():
    text = ""
    letter = 0
    for index in range(len(keysList)):
        key = tuple(map(lambda x: int(x), keysList[index].translate(str.maketrans('', '', ',' '(' ')' '\n')).split(" ")))
        if index % 2 == 0:
            text += chr(letter)
            letter = 0
        if index % 2 == 0:
            red = pix[key][0] & imgMask
            red <<= 6
            letter |= red
            blue = pix[key][2] & imgMask
            blue <<= 4
            letter |= blue
        else:
            red = pix[key][0] & imgMask
            red <<= 2
            letter |= red
            blue = pix[key][2] & imgMask
            letter |= blue
    print(text)
    keys.close()
    img.close()
            
decoder()



