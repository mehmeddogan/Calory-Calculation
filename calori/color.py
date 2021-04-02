import cv2
import numpy as np


def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    return cv2.resize(image, dim, interpolation=inter)


deger = 3000
adet = 0
kontrol = 0
degerlistesi = []
renk = ''

img = cv2.imread("pizza.png")
img = cv2.resize(img, (640,480), interpolation=cv2.INTER_AREA)
#cv2.imshow("Original Image", img)

img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
img_yuv[:, 0, :] = cv2.equalizeHist(img_yuv[:, 0, :])
img_yuv[0, :, :] = cv2.equalizeHist(img_yuv[0, :, :])
# convert the YUV image back to RGB format
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

hsv = cv2.cvtColor(img_output, cv2.COLOR_BGR2HSV)

red_lower = np.array([178, 179, 0], np.uint8)
red_upper = np.array([255, 255, 255], np.uint8)

black_lower= np.array([0,0,0], np.uint8)
black_upper= np.array([100,100,100], np.uint8)

blue_lower = np.array([91, 80, 125], np.uint8)
blue_upper = np.array([130, 255, 255], np.uint8)

yellow_lower = np.array([22, 0, 50], np.uint8)
yellow_upper = np.array([90, 255, 255], np.uint8)

green_lower = np.array([28,123,42], np.uint8)
green_upper= np.array([252,252,255], np.uint8)

red = cv2.inRange(hsv, red_lower, red_upper)
blue = cv2.inRange(hsv, blue_lower, blue_upper)
yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
black = cv2.inRange(hsv,black_lower, black_upper)
green = cv2.inRange(hsv, green_lower, green_upper)
kernel = np.ones((8, 8), "uint8")

red = cv2.dilate(red, kernel)
res = cv2.bitwise_and(img, img, mask=red)

cv2.imshow('red',red)
cv2.imshow('red',res)

blue = cv2.dilate(blue, kernel)
res1 = cv2.bitwise_and(img, img, mask=blue)

#cv2.imshow('blue',blue)
#cv2.imshow('blue',res1)

yellow = cv2.dilate(yellow, kernel)
res2 = cv2.bitwise_and(img, img, mask=yellow)

cv2.imshow('yellow',yellow)
cv2.imshow('yellow',res2)

black = cv2.dilate(black, kernel)
res3 = cv2.bitwise_and(img, img, mask=black)
cv2.imshow('black',black)
cv2.imshow('black',res3)

green = cv2.dilate(green, kernel)
res4 = cv2.bitwise_and(img, img, mask=green)

cv2.imshow('green',green)
cv2.imshow('green',res4)

rgy = red + blue + yellow + black + green

imaj = res + res1 + res2 + res3 + res4
# cv2.imshow('imajim', imaj)

contours, hierarchy = cv2.findContours(rgy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
calory_zeytin=17.25 # bir adet
calory_biber = 20 # bir adet
calry_peynir = 175 # 50 gr
# contours = contours[0] if imutils.is_cv2() else contours[1]
yellow_countours = 0
blackCountours = 0
greenContours = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if (area > deger):
        M = cv2.moments(contour)
        if int(M['m00']) > 0:
            cX = int(M['m10'] / M['m00'])
            cY = int(M['m01'] / M['m00'])

            b, g, r = cv2.split(hsv)

            b_mean = b[cY][cX]
            g_mean = g[cY][cX]
            r_mean = r[cY][cX]


            if 136 <= b_mean <= 180 and 87 <= g_mean <= 255 and 111 <= r_mean <= 255:
                cv2.putText(img, "RED", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
                degerlistesi.append("RED")
                renk += renk + str('0')
                # degerlistesi.append(cX)
                # degerlistesi.append(cY)
            elif 91 <= b_mean <= 130 and 80 <= g_mean <= 255 and 125 <= r_mean <= 255:
                cv2.putText(img, "BLUE", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
                degerlistesi.append("BLUE")
                renk += renk + str('1')
                # degerlistesi.append(cX)
                # degerlistesi.append(cY)
            elif 0 <= b_mean <= 55 and 3 <= g_mean <= 36 and 0 <= r_mean <= 41:
                blackCountours = blackCountours + 1
                cv2.putText(img, "BLACK", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
                degerlistesi.append("BLACK")
                renk += renk + str('1')

                # degerlistesi.append(cX)
                # degerlistesi.append(cY)
            elif 14 <= b_mean <= 36 and 110 <= g_mean <= 133 and 110 <= r_mean <= 135:
                greenContours += 1
                print(greenContours)
                cv2.putText(img, "GREEN", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
                degerlistesi.append("GREEN")
                renk += renk + str('1')
                # degerlistesi.append(cX)
                # degerlistesi.append(cY)
            else:
                # if b_mean >= 20 and b_mean <= 80 and g_mean >= 0 and g_mean <= 255 and r_mean >=50 and r_mean <= 255:
                cv2.putText(img, "YELLOW", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)
                degerlistesi.append("YELLOW")
                renk += renk + str('2')
                yellow_countours+= 1
                print(yellow_countours)
                # degerlistesi.append(cX)
                # degerlistesi.append(cY)

    if (len(renk) > 16):
        renk = renk[0:15]
    else:
        for index in range(0, len(renk)):
            renk += renk + str(0)
    print(renk)
print("***")
print(degerlistesi)

      # Create window with freedom of dimensions
imS = ResizeWithAspectRatio(img, width=640)        # Resize image
cv2.imshow('Video', imS)
print(blackCountours)
print("peynirin kalorisi:",calry_peynir*yellow_countours,"calory")
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()