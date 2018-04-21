import cv2
import numpy as np

faces=cv2.CascadeClassifier("C:\\Users\\Rohan\\Desktop\\Python\\Open CV code\\haarcascade_frontalface_default.xml")

img=cv2.imread("C:\\Users\\Rohan\\Desktop\\Python\\Open CV code\\group.jpeg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
value=faces.detectMultiScale(gray,1.35,5)
print "Number of faces: ",len(value)

for (x,y,w,h) in value:
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,255,0),2)
cv2.imshow("Detection",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
