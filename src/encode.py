import cv2
import time


def readImage(path):
    return cv2.imread(path)


def getRedValues(image):
    [w, h] = image.shape[:2]
    redValues = []
    for i in range(h):
        for j in range(w):
            rgb = image[j, i]
            red = rgb[0]
            redValues.append(red)
    return redValues


def getBin(number, index):
    res = 0
    for i in range(index + 1):
        res = number % 2
        number = number // 2
    return res


def encode(image):

    redValues = getRedValues(image)

    messBin = []
    indexEight = 0
    numberBin = 0

    for i in range(len(redValues)):
        red = redValues[i]
        numberBin = numberBin + ((red % 2) * pow(2, indexEight))

        indexEight = indexEight + 1

        if indexEight == 8:
            # print(numberBin)
            if numberBin != 0:
                messBin.append(numberBin)
            numberBin = 0
            indexEight = 0

    res = ""
    for i in range(len(messBin)):
        res = res + chr(messBin[i])
    return res


img = readImage(
    "/Users/icongkhanh/Desktop/MyProjects/thong-tin-ban-quyen-anh/decode.png")

print("Loading...")
message = encode(img)
print(message)
