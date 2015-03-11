""" Experiment with face detection and image filtering using OpenCV

edited and completed toolbox by Manik Singh Sethi

 """

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('/home/msethi/Downloads/haarcascade_frontalface_alt.xml') #location of the file (had to seperately download)
kernel = np.ones((30,30),'uint8') #upped the blurring a bit

cap = cv2.VideoCapture(0)

while(True):
     # Capture frame-by-frame
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20)) #detects the face
    for (x,y,w,h) in faces:
    	frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
    	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255)) #finds the rectangle aroundn the face
    	cv2.circle(frame, (x+w/4+15, y+h/4+40), 15, (255,255,255), -1, 8, 0)  #two lines drow whites of eyes
    	cv2.circle(frame, (x+3*w/4-15, y+h/4+40), 15, (255,255,255), -1, 8, 0)
    	cv2.circle(frame, (x+w/4+15, y+h/4+40), 7, (0,0,0), -1, 8, 0) #two lines draw pupils
    	cv2.circle(frame, (x+3*w/4-15, y+h/4+40), 7, (0,0,0), -1, 8, 0)
    	cv2.line(frame, (x+w/4,y+h/4+25), (x+w/4+120/4,y+h/4+25), (0,0,0), 5,8,0)  #two lines draw eyebrows
    	cv2.line(frame, (x+3*w/4,y+h/4+25), (x+3*w/4-30,y+h/4+25), (0,0,0), 5,8,0)
    	cv2.ellipse(frame, (x+w/2, y+3*h/4+20), (35,20), 180, 180, 0, (0, 0,255), -1) #draws mouth

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
