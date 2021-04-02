import numpy as np
import cv2

lower = {'blue':(110,50,50), 'yellow':(29,59,119), 'red':(0,50,80)}
upper = {'blue':(130,255,255), 'yellow':(54,255,255), 'red':(20,255,255)}
img = cv2.imread('pizza.png')
img = cv2.resize(img, (640, 460), interpolation=cv2.INTER_AREA)
hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('asd',img)
for key,value in upper.items():
    mask = cv2.inRange(hsv, lower[key],upper[key])
    cv2.imshow(key,mask)
cv2.waitKey(0)
cv2.destroyAllWindows()