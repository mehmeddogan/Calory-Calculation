import  cv2

resim = 1 #burada her klasör içindeki negatif fotoğraf sayısına göre sınır değişkenini koyuyoruz.
for i in range(11):
    img = cv2.imread(str(resim)+".jpg")
    cv2.imshow('Original', img)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("new image", gray_img)
    img_scaled = cv2.resize(img, (1366, 760), interpolation=cv2.INTER_AREA)
    #cv2.imshow('yeni boyut', img_scaled)
    cv2.imwrite('new'+str(resim)+'.jpg', img_scaled)
    resim += 1
cv2.waitKey(0)
cv2.destroyAllWindows()