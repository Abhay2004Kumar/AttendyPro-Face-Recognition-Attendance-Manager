from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Student_details import Student
import os
from time import strftime
from datetime import datetime
import numpy as np
import cv2
from tkinter import messagebox
import mysql.connector
import difflib
from Attendance import Attendance


class face_scan:
    def __init__(self, root):
        self.root = root
        # Set geometry of window
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendy-Pro")

        img=Image.open("GUI images/iiitu.JPG")
        img=img.resize((1530,250)) #ANTIALIAS CONVERT HIGH LEVEL TO LOW LEVEL IMAGE
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=250)

        #bg image
        img1=Image.open("GUI images/bg.PNG")
        img1=img1.resize((1530,790)) #ANTIALIAS CONVERT HIGH LEVEL TO LOW LEVEL IMAGE
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_lbl=Label(self.root,image=self.photoimg1)
        bg_lbl.place(x=0,y=250,width=1530,height=790)

        #TITLE
        title_lbl = Label(bg_lbl,text="AttendyPro",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=58)

        #registration button
        img2=Image.open("GUI images/student.PNG")
        img2=img2.resize((120,120)) 
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(bg_lbl,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=120,height=120)

        b1_1=Button(bg_lbl,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",13,"bold"),bg="white",fg="black")
        b1_1.place(x=200,y=200,width=120,height=40)

        #detect face button
        img3=Image.open("GUI images/detect.PNG")
        img3=img3.resize((120,120)) 
        self.photoimg3=ImageTk.PhotoImage(img3)

        b2=Button(bg_lbl,image=self.photoimg3,cursor="hand2")
        b2.place(x=700,y=100,width=120,height=120)

        b2_1=Button(bg_lbl,text="Detect Face",cursor="hand2",command=self.face_recog,font=("times new roman",13,"bold"),bg="white",fg="black")
        b2_1.place(x=700,y=200,width=120,height=40)

         #attendance button
        img4=Image.open("GUI images/attendance.PNG")
        img4=img4.resize((120,120)) 
        self.photoimg4=ImageTk.PhotoImage(img4)

        b3=Button(bg_lbl,image=self.photoimg4,command=self.Attendance,cursor="hand2")
        b3.place(x=1200,y=100,width=120,height=120)

        b3_1=Button(bg_lbl,text="Attendance",command=self.Attendance,cursor="hand2",font=("times new roman",13,"bold"),bg="white",fg="black")
        b3_1.place(x=1200,y=200,width=120,height=40)

         #Train face button
        img5=Image.open("GUI images/machine-learning.PNG")
        img5=img5.resize((120,120)) 
        self.photoimg5=ImageTk.PhotoImage(img5)

        b4=Button(bg_lbl,image=self.photoimg5,cursor="hand2")
        b4.place(x=200,y=300,width=120,height=120)

        b4_1=Button(bg_lbl,text="Data Training",cursor="hand2",command=self.train_classifier,font=("times new roman",13,"bold"),bg="white",fg="black")
        b4_1.place(x=200,y=412.5,width=120,height=40)

         #photo collect button
        img6=Image.open("GUI images/data-collection.PNG")
        img6=img6.resize((120,120)) 
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b6=Button(bg_lbl,image=self.photoimg6,command=self.open_img,cursor="hand2")
        b6.place(x=700,y=300,width=120,height=120)

        b6_1=Button(bg_lbl,text="Collect Photos",command=self.open_img,cursor="hand2",font=("times new roman",13,"bold"),bg="white",fg="black")
        b6_1.place(x=700,y=412.5,width=120,height=40)

         #Exit button
        img7=Image.open("GUI images/exit.PNG")
        img7=img7.resize((120,120)) 
        self.photoimg7=ImageTk.PhotoImage(img7)

        b7=Button(bg_lbl,image=self.photoimg7,command=self.iexit,cursor="hand2")
        b7.place(x=1200,y=300,width=120,height=120)

        b7_1=Button(bg_lbl,text="Exit",command=self.iexit,cursor="hand2",font=("times new roman",13,"bold"),bg="white",fg="black")
        b7_1.place(x=1200,y=412.5,width=120,height=40)

    def iexit(self):
        self.iexit=messagebox.askyesno("Attendy Pro","Are you sure exit this project")
        if self.iexit>0:
            self.root.destroy()
        else:
            return


        





    def open_img(self):
        os.startfile("Data")


        #function to goto student page
    
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.switch=Student(self.new_window)
    
    def Attendance(self):
        self.new_window=Toplevel(self.root)
        self.switch=Attendance(self.new_window)

    #train classifier
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("D:/coding/Practicum_IV_project/classifier.xml")
        cv2.destroyAllWindows
        messagebox.showinfo("Result","Training datasets completed")


    #function to mark attendance
    def attendance_marker(self,id,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            id_list=[]
            for line in myDataList:
                entry=line.split((","))
                if entry[0].isnumeric():
                    id_list.append(int(entry[0]))
                print(id_list)
            if((id not in id_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{id},{n},{d},{dtString},{d1},Present")



                

     

    #face recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scalefactor,minNeighbous,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scalefactor,minNeighbous)

            coordinates=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                print(id)
                conn=mysql.connector.connect(host="localhost",username="root",password="Lucifer2004Kumar",database="FACE_RECOGNITION_ATTENDANCE_MANAGER")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student_details where StudentID="+str(id))
                n=my_cursor.fetchone()
                if n!=None:
                    n="+".join(n)
                else:
                    n = "  "

                my_cursor.execute("select Department from student_details where StudentID="+str(id))
                r=my_cursor.fetchone()
                if r!=None:
                    r="+".join(r)
                else:
                    r = "  "

                

                    

               
                
    



                if confidence>78:
                    cv2.putText(img,f"Id: {id}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name: {n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department: {r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    if id != None:
                        self.attendance_marker(id,n,r)
    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown identity",(x,y-20),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coordinates=[x,y,w,h]

            return coordinates
        
        def recognizer(img,clf,faceCascade):
            coordinates=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture=cv2.VideoCapture(0)

        while True:
            ret,img=video_capture.read()
            img=recognizer(img,clf,faceCascade)
            cv2.imshow("Face Recognition Window",img)

            if cv2.waitKey(1)==13:
                video_capture.release()
                cv2.destroyAllWindows()
                break
            
          



if __name__ == "__main__":
    root = Tk()
    # Making object of the class
    obj = face_scan(root)
    root.mainloop()
