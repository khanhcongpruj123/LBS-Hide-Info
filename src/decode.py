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
    # chen thong tin ban quyen vao gia tri cac bit thap cua mau do trong anh
    redValues = getRedValues(image)

    messAscii = getAciiFromString(message)

    # chi so cho day message da duoc chuyen thanh ma ascii
    indexMess = 0

    # chi so bit cua tung tu trong message, o day dung 8 bit de bieu dien 1 tu, indexEight se
    # tang dan tu 0 den 7 tuong ung voi 2^0, 2^1,... den khi bang 8 thi se quay nguoc lai bang 0
    # de gan tu moi
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

    # tao ma tran diem anh moi da decode
    [w, h] = image.shape[:2]
    index = 0
    resImg = img
    for i in range(h):
        for j in range(w):
            resImg[j, i, 0] = redValues[index]
            index = index + 1

    # luu anh vua decode
    cv2.imwrite("./assets/decode/decode.png", img)

# ====================== main ===========================


img = cv2.imread(
    "./assets/img.jpg")
message = input("Enter your message: ")

print("Loading...")
decodeImage(message, img)
print("Done!")

# ====================== main ===========================
