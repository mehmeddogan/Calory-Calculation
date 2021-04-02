import cv2
import numpy as np
from matplotlib import pyplot as plt
array=1
img = cv2.imread('pizza.png',1)
img = cv2.resize(img, (640, 460), interpolation=cv2.INTER_AREA)
#resized = cv2.resize(img, (500,500), interpolation = cv2.INTER_AREA)
bilateral_blur = cv2.bilateralFilter(img, 9, 75, 75)
edges = cv2.Canny(bilateral_blur, 100, 200)
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.HuMoments(cv2.moments(image)).flatten()
array = ([  6.53608067e-04,   6.07480284e-16,   9.67218398e-18,
         1.40311655e-19,  -1.18450102e-37,   8.60883492e-28,-1.12639633e-37])
cv2.imshow("original", img)
cv2.imshow("new", bilateral_blur)
cv2.imshow("edges",edges)
#moments = cv2.moments([0],img)
#huMoments = cv2.HuMoments(moments)
cv2.waitKey(0)
cv2.destroyAllWindows()