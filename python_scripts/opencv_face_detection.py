import cv2
# img = cv2.imread('people.jpg')
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   # 載入人臉模型
        
while True:
    success, img = cap.read()
    if success:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 將圖片轉成灰階
        faces = face_cascade.detectMultiScale(gray)    # 偵測人臉
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)    # 利用 for 迴圈，抓取每個人臉屬性，繪製方框

        cv2.imshow('oxxostudio', img)
    if cv2.waitKey(60) == ord('q'):
        break
cv2.destroyAllWindows()