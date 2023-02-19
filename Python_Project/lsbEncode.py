from PIL import Image, ImageDraw
from random import randint

def encoderMain(imageFile, userText):
    try:
        img = Image.open(imageFile)
        draw = ImageDraw.Draw(img)
        pix = img.load()
    except:
        return "Chosen image file is not an image"
    keys = open("keys.txt", "w+")
    text = userText
    imageName = imageFile.split("/")
    return encoder(img, draw, pix, keys, text, imageName)

imgMask = 0b11111100
textMask = 0b11000000
indexForRGB = [0, 2, 0, 2]

def encoder(img, draw, pix, keys, text, imageName):
    width = img.size[0]
    height = img.size[1]
    index = 0
    while index < len(text):
        letter = ord(text[index])
        key = randint(0, width - 10), randint(0, height - 10)
        for i in range(0, 4):
            colorCode = pix[key][indexForRGB[i]] & imgMask
            letterMask = letter & textMask
            letterMask >>= 6
            colorCode |= letterMask
            encodeInImage(colorCode, key, i, draw, pix, keys)
            letter <<= 2
            if i == 1:
                key = randint(0, width - 10), randint(0, height - 10)
        index += 1
    img.save("new" + editImageName(imageName[len(imageName) - 1]), imageFormat(imageName[len(imageName) - 1]))
    keys.close()
    return "Text is encoded\nImage and file with keys are in the program folder"

def encodeInImage(colorCode, key, index, draw, pix, keys):
    if index == 0 or index == 2:
        draw.point(key, (colorCode, pix[key][1], pix[key][2]))
    elif index == 1 or index == 3:
        draw.point(key, (pix[key][0], pix[key][1], colorCode))
    if index == 1 or index == 3:
        keys.write(str(key) + "\n")

def imageFormat(imageName):
    if ".png" in imageName or ".jpg" in imageName or ".jpeg" in imageName:
        return "PNG"
    elif ".bmp" in imageName:
        return "BMP"

def editImageName(imageName):
    if imageName.split(".")[1] == "jpg" or imageName.split(".")[1] == "jpeg":
        return imageName.split(".")[0] + ".png"
    elif imageName.split(".")[1] == "png":
        return imageName.split(".")[0] + ".png"
    elif imageName.split(".")[1] == "bmp":
        return imageName.split(".")[0] + ".bmp"