import cv2
import numpy as np
img = cv2.imread('foto.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

low_red=np.array([22,109,219])
upper_red = np.array([255,255,255])
mask = cv2.inRange(hsv, low_red,upper_red)
res = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('frame', img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)


cv2.waitKey(0)
cv2.destroyAllWindows()
img.release()