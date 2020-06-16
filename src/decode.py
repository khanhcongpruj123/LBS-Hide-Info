import cv2
import numpy
import time


def readImage(path):
    return cv2.imread(path)


def getRedValues(image):
    [w, h] = image.shape[:2]
    redValues = []
    for i in range(h):
        for j in range(w):
            red = image[j, i, 0]
            redValues.append(red)
    return redValues


def getAciiFromString(message):
    res = []
    for i in range(len(message)):
        a = ord(message[i])
        res.append(a)
    return res


def checkValidMessage(message, image):
    asciis = getAciiFromString(message)
    size = len(asciis) * 8
    [w, h] = image.shape[:2]
    if size > w * h:
        return False
    return True


def getBin(number, index):
    res = 0
    for i in range(index + 1):
        res = number % 2
        number = number // 2
    return res


def decodeImage(message, image):
    if checkValidMessage(message, image) == False:
        return

    redValues = getRedValues(image)
    messAscii = getAciiFromString(message)

    indexMess = 0
    indexEight = 0
    sizeMess = len(messAscii)

    # chen thong tin ban quyen duoi dang bit vao bit thap cua anh
    for i in range(len(redValues)):
        red = redValues[i]

        # xoa bit thap cua anh
        if red % 2 == 1:
            red = red - 1

        # kiem tra xem da chen het thong tin hay chua?
        if indexMess < sizeMess:
            red = red + getBin(messAscii[indexMess], indexEight)
            indexEight = indexEight + 1
            if indexEight == 8:
                indexMess = indexMess + 1
                indexEight = 0

        redValues[i] = red

    [w, h] = image.shape[:2]
    index = 0
    resImg = img
    for i in range(h):
        for j in range(w):
            resImg[j, i, 0] = redValues[index]
            index = index + 1

    # luu anh vua decode
    cv2.imwrite("decode.png", img)


img = cv2.imread(
    "/Users/icongkhanh/Desktop/MyProjects/thong-tin-ban-quyen-anh/assets/img.jpg")
message = "Khanh Yeu Vy Rat Nhieu!"

print("Loading...")
decodeImage(message, img)
print("Done!")
