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

    # lay cac gia tri mau do de doc thong tin da decode
    redValues = getRedValues(image)

    # chua cac ma ascii cua cac tu
    messBin = []

    # chi so bit cua tung tu trong message, o day dung 8 bit de bieu dien 1 tu, indexEight se
    # tang dan tu 0 den 7 tuong ung voi 2^0, 2^1,... den khi bang 8 thi se quay nguoc lai bang 0
    # de gan tu moi
    indexEight = 0

    # dung de luu gia tri ma ascii cua tu dang duoc encode
    numberBin = 0

    # lay gia tri bit thap cua cac mau do sau do gan vao numerBin, sau khi hoan thanh xong 8 bit
    # thi bo vao messBin
    for i in range(len(redValues)):
        red = redValues[i]
        numberBin = numberBin + ((red % 2) * pow(2, indexEight))

        indexEight = indexEight + 1

        if indexEight == 8:
            if numberBin != 0:
                messBin.append(numberBin)
            numberBin = 0
            indexEight = 0

    # chuyen tat ca ma ascii trong messBin thanh string
    res = ""
    for i in range(len(messBin)):
        res = res + chr(messBin[i])
    return res

# ====================== main ===========================


img = readImage(
    "./assets/decode/decode.png")

print("Loading...")
message = encode(img)
print(message)

# ====================== main ===========================
