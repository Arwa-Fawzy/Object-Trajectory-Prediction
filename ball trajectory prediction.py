from sre_constants import SUCCESS
from tkinter import Image
import cv2 as cv
import cvzone as cvz
from cv2 import resize
from cvzone.ColorModule import ColorFinder
import numpy as np

#assign the video into a variable 
shot=cv.VideoCapture('D:/CS/Robotics club/basketball/video.mp4')

#create object color finder 
myColor=ColorFinder(False)
HSVvalues={'hmin': 0, 'smin': 72, 'vmin': 25, 'hmax': 12, 'smax': 187, 'vmax': 198}
positionFramesx=[]
positionFramesy=[]
xPoints=[i for i in range (0,1000)]

while True:
    #reading the shot's data: the video and the image
    success , img=shot.read()
    #img=cv.imread("D:/CS/Robotics club/basketball/img.png") 
    img=img[0:900, :]

    #detect the color of the ball
    imgColor, point= myColor.update(img,HSVvalues)

    #location of the ball
    ballContours, contours=cvz.findContours(img,point, minArea=500)

    #if there is a contour, take the biggest contour value (contour array is sorted
    # with zero based indexing) with the center point of it

    #To display all the frames, not only the current one

    if contours:
        positionFramesx.append(contours[0]['center'][0])
        positionFramesy.append(contours[0]['center'][1])
        #to determine it in a circle with (cx,xy) coordinates for center point
        #with center =3 with filled thickness and red color according to RGB
    if positionFramesx:
        #regression equation and finding the coffcients
        #ax^2+bx+c
        a,b,c=np.polyfit(positionFramesx, positionFramesy,2)
        

        for j,(x,y) in enumerate (zip(positionFramesx,positionFramesy)):
            i=(x,y)
            cv.circle(ballContours, i, 9, (0,0,255), cv.FILLED) 
            print(i)
            if j==0:
                cv.line(ballContours,i,i,(0,255,0),2) 
            else:
                cv.line(ballContours,i,(positionFramesx[j-1],positionFramesy[j-1]),(0,255,0),2)
        for x in xPoints:
            y=int(a*(x**2)+b*x+c)
            cv.circle(ballContours, (x,y), 3, (0,255,0), cv.FILLED) 


    
    #choose an appropriate size to show the shot 
    img=cv.resize(img, (0,0),None, 0.7,0.7)
    #cv.imshow("Image",img)
    ballContours=cv.resize(ballContours, (0,0),None, 0.7,0.7)
    cv.imshow("imgColor",ballContours)

    #the delay value is  as the shot is fast 
    cv.waitKey(1)


    