import cv2
import numpy as np

zeytinCascade = cv2.CascadeClassifier('zeytin.xml')
biberCascade = cv2.CascadeClassifier('biber.xml')
domatesCascade = cv2.CascadeClassifier('domates.xml')
sucukCascade = cv2.CascadeClassifier('sucuk.xml')
misirCascade = cv2.CascadeClassifier('misir.xml')
mantarCascade = cv2.CascadeClassifier('mantar.xml')

img = cv2.imread('pizza.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

red = np.array([30,150,50])
upper_red = np.array([255,255,180])

mask = cv2.inRange(hsv, red, upper_red)
res = cv2.bitwise_and(img,img, mask= mask)
zeytin = zeytinCascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5, flags=0, minSize=(10, 10), maxSize=(50, 50))
biber = biberCascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5, flags=0, minSize=(10, 10), maxSize=(50, 50))
domates = domatesCascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5, flags=0, minSize=(10, 10), maxSize=(50, 50))
sucuk = sucukCascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5, flags=0, minSize=(10, 10), maxSize=(50, 50))
misir = misirCascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5, flags=0, minSize=(10, 10), maxSize=(50, 50))
mantar = mantarCascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5, flags=0, minSize=(10, 10), maxSize=(50, 50))

print(type(zeytin))
print(zeytin)

for x,y,w,h in zeytin:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)

cv2.imshow('Gray', img)
cv2.waitKey(0)
cv2.destroyAllWindows()