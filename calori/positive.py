import cv2

resim = 1   #n = pozitif fotoğraf sayısı
for i in range(n):
    img = cv2.imread(str(resim)+".jpg")
    cv2.imshow('Original', img)
    img_scaled = cv2.resize(img, (1366, 760), interpolation=cv2.INTER_AREA)
    #cv2.imshow('yeni boyut', img_scaled)
    cv2.imwrite('new'+str(resim)+'.jpg', img_scaled)
    resim += 1
cv2.waitKey(0)
cv2.destroyAllWindows()