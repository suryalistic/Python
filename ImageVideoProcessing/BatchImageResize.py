import glob,cv2,os,pprint,datetime

def readimages(path):
    os.chdir(path)
    jpgList = glob.glob('*.jpg')
    pprint.pprint(jpgList)
    return jpgList
def resize(imgs):
    outdirName = 'resized'+(datetime.datetime.now().strftime('%Y-%m-%d::%H-%M-%S'))
    os.mkdir(outdirName)
    os.chdir(outdirName)
    for img in imgs:
	pprint.pprint(img)
        image = cv2.imread(img,0)
        pprint.pprint(image)
        cv2.imshow('original',image)
        cv2.waitkey(2000)
        re_image = cv2.resize(image,(100,100))
        cv2.imshow('resized',re_image)
        cv2.waitkey(2000)
        cv2.imwrite('resized_'+img,re_image)
        cv2.destroyAllWindows()
        #print(image)
def main():
    path = '/home/suryam/development/pworkspace/ImageVideoProcessing/images'
    resize(readimages(path))
main()
