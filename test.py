import cv2

#img = cv2.imread("face_1.jpg")

#a = cv2.resize(img, (400, 400))  # resize可設定顯示圖片的大小

#cv2.imshow("My Image", a)

#cv2.waitKey(0) #đợi kkhi thoát ảnh là dừng chạy chương trình
#cv2.destroyAllWindows()#phòng việc lãng phí tài nguyên

#import cv2

#img = cv2.imread("face_1.jpg")

#blur = cv2.GaussianBlur(img, (1, 1), 0) #phải là số lẻ

#a = cv2.resize(blur, (400, 400))

#cv2.imshow("My Image", a)

#cv2.waitKey(0)

#cv2.destroyAllWindows()

#import cv2
#img = cv2.imread("face_1.jpg")
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#edge = cv2.Canny(gray, 100, 200)
#a= cv2.resize(edge, (400, 400))
#cv2.imshow("My Image", a)
#cv2.waitKey(0)
#cv2.destroyAllWindows() #chuyen thanh nen den va dua ra dac diem cu the nhat

import os

input = "1"  #讀入資料夾 1

output = "2" #儲存資料夾 2

os.makedirs(output, exist_ok=True)