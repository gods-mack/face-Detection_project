import cv2,time
import sys


face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('data/haarcascade_eye.xml')
video_capture = cv2.VideoCapture(0)


a = 1
""" check = bool data type return Trupe if Python
     able to read the videoCapture
    frame = NUmpy array containf first image capture by object """
while True:
     a = a+1
     check,frame = video_capture.read() 
     #time.sleep(3)  # helps to run camara for 3second
     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray,1.3,5)
     for (x,y,w,h) in faces:
       cv2.rectangle(frame,(x,y),(x+w,y+h), (255,0,0),2)
       roi_gray = gray[y:y+h, x:x+w]
       roi_color = frame[y:y+h, x:x+w]
       eyes = eye_cascade.detectMultiScale(roi_gray) 
       for (ex,ey,ew,eh) in eyes:
          cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,9),2)
     cv2.imshow('Capturing',frame)
     key = cv2.waitKey(1)
     if(key == ord('q')): 
       break


print(a)
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
