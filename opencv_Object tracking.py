import cv2
import numpy as np
import imutils

cam = cv2.VideoCapture(0)

while True:
    _,frame=cam.read()
    frame=imutils.resize(frame,width=500)

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_blue= np.array([100,100,100])
    upper_blue= np.array([120,255,255])

    mask= cv2.inRange(hsv, lower_blue, upper_blue)
    mask= cv2.erode(mask,None,iterations=1)
    mask= cv2.dilate(mask,None,iterations=1)

    cont=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,
                          cv2.CHAIN_APPROX_SIMPLE)[-2]
    center=None
    if len(cont)>0:
        
        c = max(cont, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius),(0,0,255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('LIVE',frame)
##    cv2.imshow('BLUE',res)

    
    
    k=cv2.waitKey(5)
    if k==27:
        break

cam.release()
cv2.destroyAllWindows()
