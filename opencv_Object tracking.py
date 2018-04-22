import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    _,img=cam.read()
    img=cv2.flip(img,1)

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower= np.array([0,0,0])
    upper= np.array([0,0,255])

    mask= cv2.inRange(hsv, lower, upper)

    cont=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,
                          cv2.CHAIN_APPROX_SIMPLE)[-2]
    center=None
    if len(cont)>0:
        
        c = max(cont, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        if radius > 10:
            cv2.circle(img, (int(x), int(y)), int(radius),(0,0,255),2)
            cv2.circle(img, center, 5, (0, 0, 255), -1)
##            print len(center)

##    print len(cont)
    
    res=cv2.bitwise_and(img,img,mask=mask)
    
    cv2.imshow('LIVE',img)
##    cv2.imshow('BLUE',res)

    
    
    k=cv2.waitKey(5)
    if k==27:
        break

cam.release()
cv2.destroyAllWindows()
