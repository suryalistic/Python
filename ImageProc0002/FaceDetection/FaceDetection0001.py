import cv2,os, pprint

faces_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print(faces_cascade)
img = cv2.imread('news.jpg')
img_grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
pprint.pprint(img_grayscale)

faces = faces_cascade.detectMultiScale(img_grayscale,scaleFactor=1.05,minNeighbors=5)
print(faces)

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

cv2.imshow("result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
