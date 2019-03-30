import numpy as np
import cv2 as cv
from tkinter import *
from tkinter.filedialog import *


#button1 = Button(window,text="Upload",fg="black",bg="gray",command=upload).pack()

img = []

class eye:

   	
   def __init__(self,master):
   	 frame  = Frame(master)
   	 frame.pack()
   	 button1 = Button(frame,text="Upload",fg="green",bg="gray",command=self.upload).pack()
     #quit_button = Button(frame, text ="Quit",bg="Red",fg="green",command=frame.destroy).pack()
   	 

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

    #def exit(self):

    
   
    


#button1 = Button(window,text="Upload",fg="black",bg="gray",command=obj.upload).pack()
#button1 = Button(window,text="Upload",fg="black",bg="green",command=disp).pack()
def quit(root): 	
 root.destroy() 
root = Tk()
root.title("FaceIt___")
root.geometry("500x500")
button2 = Button(root,text="Exit",fg="green",bg="red",command=lambda root=root:quit(root)).pack()
root.configure(background="black")
obj  = eye(root)
#button1 = Button(root,text="Exit",fg="green",bg="red",command=lambda root=root:quit(root)).pack()
root.mainloop()
