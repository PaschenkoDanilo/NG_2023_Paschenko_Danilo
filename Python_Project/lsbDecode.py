from PIL import Image, ImageDraw

def decoderMain(imgFile, keysFile):
    try:
        img = Image.open(imgFile)
        draw = ImageDraw.Draw(img)
        pix = img.load()
    except:
        return "Chosen image file is not an image"
    keys = open(keysFile, "r")
    try:
        keysList = list([key for key in keys])
    except:
        return "Chosen keys file has no keys or the keys are corrupted"
    return decoder(pix, keys, keysList)

imgMask = 0b00000011
indexForRGB = [0, 2, 0, 2]

def decoder(pix, keys, keysList):
    text = ""
    index = 0
    while index < len(keysList):
        letter = 0
        try:
            key = tuple(map(lambda x: int(x), keysList[index].translate(str.maketrans('', '', ',' '(' ')' '\n')).split(" ")))
        except:
            return "Chosen keys file has no keys or the keys are corrupted"
        for i in range(0, 4):
            colorCode = pix[key][indexForRGB[i]] & imgMask
            letter <<= 2
            letter |= colorCode
            if i == 1:
                index += 1
                key = tuple(map(lambda x: int(x), keysList[index].translate(str.maketrans('', '', ',' '(' ')' '\n')).split(" ")))
        index += 1
        text += chr(letter)
    keys.close()
    return text