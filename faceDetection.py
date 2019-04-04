import numpy as np
import cv2 as cv
from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import *
import os


#button1 = Button(window,text="Upload",fg="black",bg="gray",command=upload).pack()

img = []

class eye:

   """Here We Placed Button and read Instruction  label """
   def __init__(self,master):
     frame  = Frame(master)   # Top frame
     frame.pack()
     button1 = Button(frame,text="Upload",fg="white",bg="gray",width=7,height=2,command=self.upload).pack(side="left")
     button2 = Button(frame,text="Real Time",fg="white",bg="gray",width=7,height=2,command=self.realtime).pack(side="right")
     dire0 = Label(master,text="read instruction:  ",fg="green")
     dire0.config(font=('Helvetica',13))
     dire0.pack()
     dire1 = Label(master,text="upload Button : to detect face from existing image(in computer)",fg="red")
     dire1.config(font=('helvetica',14))
     dire1.pack()
     dire2 = Label(master,text="real time Button  : detect Face from live WebCam",fg="red")
     dire2.config(font=('Helvetica',14))
     dire2.pack()
     dire3 = Label(master,text="Press 'q' to disable Webcam ",fg="red")
     dire3.config(font=('Helvetica',14))
     dire3.pack()
     
     
   """In Upload Function we will Upload an image from Our Computer 
   Directory
   and then convert original image in Gray Scale Image
   apply haarcasCade Classifier in Gray Scale image to scan face part """
   def upload(self):
     imgTemp  = askopenfilename()
     img = cv.imread(imgTemp)
     img = np.array(img, dtype=np.uint8)  
     face_cascade = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
     eye_cascade = cv.CascadeClassifier('data/haarcascade_eye.xml')
     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray, 1.3, 5)

     for (x,y,w,h) in faces:
      cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
      roi_gray = gray[y:y+h, x:x+w]
      roi_color = img[y:y+h, x:x+w]
      eyes = eye_cascade.detectMultiScale(roi_gray)
      for (ex,ey,ew,eh) in eyes:
         cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
     
     cv.imshow('img',img)
     cv.waitKey(0)
     cv.destroyAllWindow()  
  # Here we have have real time face detection Module
   def realtime(self):
     face_cascade = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
     eye_cascade = cv.CascadeClassifier('data/haarcascade_eye.xml')
     video_capture = cv.VideoCapture(0)


     a = 1
     """ check , bool data type return True if Python
     able to read the videoCapture
      frame = it is NUmpy array containf first image capture by object """
     while True:
       a = a+1
       check,frame = video_capture.read() 
       #time.sleep(3)  # helps to run camara for 3second
       gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray,1.3,5)
       for (x,y,w,h) in faces:
         cv.rectangle(frame,(x,y),(x+w,y+h), (255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]
         eyes = eye_cascade.detectMultiScale(roi_gray) 
         for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,9),2)
       cv.imshow('Capturing',frame)
       key = cv.waitKey(1)
       if(key==ord('q')):
          break
      
     video_capture.release()
     cv.destroyAllWindows()


# When everything is done, release the capture


    
""" Quit Window """
def quit(root): 	
 root.destroy() 
root = Tk()  # Tkiniter Object(Window)
root.title("FaceIt___")
root.geometry("600x300")
label1 = Label(root, 
		 text="Face Detection Application ",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").pack()
#label1 = Label(root,text="Face Detection Application ",width=67,height=13).pack()
button2 = Button(root,text="Exit",fg="green",bg="red",command=lambda root=root:quit(root)).pack()
root.configure(background="white")
obj  = eye(root)   # pass window object eye Class

root.mainloop()
