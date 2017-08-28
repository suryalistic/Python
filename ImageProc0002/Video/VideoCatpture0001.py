import cv2, os, datetime

def videocapture():
    path = 'out' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    os.mkdir(path)
    os.chdir(path)
    count = 1
    videoObject = cv2.VideoCapture(1)
    face_cascade_facade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    while True:
        capture,frameNumpy = videoObject.read()
        print(capture)
        #imag = cv2.imread(frameNumpy)
        gray_imag = cv2.cvtColor(frameNumpy,cv2.COLOR_BGR2GRAY)
        print(gray_imag)

        cv2.imshow("live", gray_imag)
        key = cv2.waitKey(1)
        saveImages(str(count),frameNumpy)
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