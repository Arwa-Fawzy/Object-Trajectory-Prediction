import cvzone 
import cv2

from cvzone.ColorModule import ColorFinder


shot =cv2.VideoCapture(0)

myColor=ColorFinder(False)
HSV={'hmin': 40, 'smin': 44, 'vmin': 58, 'hmax': 85, 'smax': 255, 'vmax': 243}
while True:
    success, img =shot.read()
    imgColor, mask= myColor.update(img, HSV)
    imgContour, contour=cvzone.findContours(img, mask, minArea=1000)

    if contour:
        data=contour[0]['center'][0],\
            contour[0]['center'][0],\
            int(contour[0]['area'])
        print(data)
    


    imgStack=cvzone.stackImages([imgContour],1,2)
    myColor.update(img,HSV)
    #cv2.imshow("Image", imgColor)
    cv2.imshow("Image Color", imgStack)
    cv2.waitKey(1)

