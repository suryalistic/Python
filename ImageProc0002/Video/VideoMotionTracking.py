import cv2, os, datetime

def videocapture():
    path = 'out' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    os.mkdir(path)
    os.chdir(path)
    count = 1
    videoObject = cv2.VideoCapture(1)
    face_cascade_facade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    base_image = None
    while True:
        capture,frameNumpy = videoObject.read()
        print(capture)
        gray_imag = cv2.cvtColor(frameNumpy,cv2.COLOR_BGR2GRAY)

        gray_gaus_img = cv2.GaussianBlur(gray_imag,(21,21),0)

        if base_image == None:
            base_image = gray_gaus_img
            continue
        gray_delta = cv2.absdiff(gray_gaus_img,base_image)

        gray_threshold_img = cv2.threshold(gray_delta,50,255,cv2.THRESH_BINARY)[1]

        (_,cnts,_) = cv2.findContours(gray_threshold_img.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #print(cnts)
        for contour in cnts:
            (x, y,w,h) = cv2.boundingRect(contour)
            cv2.rectangle(frameNumpy,(x,y),(x+w,y+h),(255,255,0),5)
        cv2.imshow("base",base_image)
        cv2.imshow("gray gaus", gray_gaus_img)
        #cv2.imshow("gray", gray_imag)
        cv2.imshow("gray delta", gray_delta)
        #cv2.imshow("gray threshold", gray_threshold_img)
        cv2.imshow("original",frameNumpy)
        key = cv2.waitKey(1)
        #saveImages(str(count),frameNumpy)
        if key == ord('q'):
            break
        count +=1
    cv2.destroyAllWindows()
    videoObject.release()

def saveImages(fname, img):
    fname += '.jpg'
    f = open(fname,'wb')
    f.write(img)
    f.close()
videocapture()