from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root

        self.var_dep= StringVar()
        self.var_year= StringVar()
        self.var_sem=StringVar()
        self.var_StID=StringVar()
        self.var_gender=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()




        # Set geometry of window
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendy-Pro")

        img=Image.open("GUI images/st_portal.JPG")
        img=img.resize((1530,275)) #ANTIALIAS CONVERT HIGH LEVEL TO LOW LEVEL IMAGE
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=275)

        #bg image
        img1=Image.open("GUI images/bg.PNG")
        img1=img1.resize((1530,790)) #ANTIALIAS CONVERT HIGH LEVEL TO LOW LEVEL IMAGE
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_lbl=Label(self.root,image=self.photoimg1)
        bg_lbl.place(x=0,y=275,width=1530,height=790)

         #TITLE
        title_lbl = Label(bg_lbl,text="STUDENTS MANAGER",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=58)

        #main frame
        main_frame=Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=20,y=63,width=1480,height=600)

        #left subframe
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",14,"bold"))
        left_frame.place(x=10,y=10,width=720,height=425)

    
        #current course
        current_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Details",font=("times new roman",12,"bold"))
        current_frame.place(x=10,y=5,width=700,height=120)

        #department
        deppt_lbl = Label(current_frame,text='Department',font=("times new roman",12,"bold"),bg="white")
        deppt_lbl.grid(row=0,column=0,padx=10,sticky=W)

        deppt_comboBox = ttk.Combobox(current_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        deppt_comboBox["values"]=("Select Department","CSE","IT","ECE")
        deppt_comboBox.current(0)
        deppt_comboBox.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Year
        year_lbl = Label(current_frame,text='Year',font=("times new roman",12,"bold"),bg="white")
        year_lbl.grid(row=0,column=2,padx=10,sticky=W)

        year_comboBox = ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_comboBox["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_comboBox.current(0)
        year_comboBox.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #semester
        semester_lbl = Label(current_frame,text='Semester',font=("times new roman",12,"bold"),bg="white")
        semester_lbl.grid(row=1,column=0,padx=10,sticky=W)

        semester_comboBox = ttk.Combobox(current_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=17,state="readonly")
        semester_comboBox["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        semester_comboBox.current(0)
        semester_comboBox.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Student class information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Details",font=("times new roman",12,"bold"))
        class_student_frame.place(x=10,y=125,width=700,height=270)

        #student id label
        student_id_lbl = Label(class_student_frame,text='StudentID:',font=("times new roman",12,"bold"),bg="white")
        student_id_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #student entry
        StudentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_StID,width=20,font=("times new roman",12,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

         #student name
        student_name_lbl = Label(class_student_frame,text='Name:',font=("times new roman",12,"bold"),bg="white")
        student_name_lbl.grid(row=1,column=0,padx=10,sticky=W)
        StudentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        StudentName_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #gender
        student_Gender_lbl = Label(class_student_frame,text='Gender:',font=("times new roman",12,"bold"),bg="white")
        student_Gender_lbl.grid(row=0,column=2,padx=10,sticky=W)
        

        StudentGender = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="readonly")
        StudentGender["values"]=("Male","Female","Others")
        StudentGender.current(0)
        StudentGender.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #email
        student_Gmail_lbl = Label(class_student_frame,text='Email:',font=("times new roman",12,"bold"),bg="white")
        student_Gmail_lbl.grid(row=1,column=2,padx=10,sticky=W)
        StudentGmail_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        StudentGmail_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #DOB
        student_DOB_lbl = Label(class_student_frame,text='DOB:',font=("times new roman",12,"bold"),bg="white")
        student_DOB_lbl.grid(row=2,column=0,padx=10,sticky=W)
        StudentDOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        StudentDOB_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #phone
        student_Phone_lbl = Label(class_student_frame,text='Phone:',font=("times new roman",12,"bold"),bg="white")
        student_Phone_lbl.grid(row=2,column=2,padx=10,sticky=W)
        StudentPhone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        StudentPhone_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        
        radio_btn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Sample",value="YES")
        radio_btn1.grid(row=5,column=0)

       
        radio_btn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Do Not Take Sample",value="NO")
        radio_btn2.grid(row=5,column=1)

        #frame for buttons
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=150,width=690,height=35)

        #save button
        save_btn = Button(btn_frame,text='SAVE',command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="red",fg="white",cursor="hand2")
        save_btn.grid(row=0,column=0)

        #update button
        update_btn = Button(btn_frame,text='UPDATE',command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="red",fg="white",cursor="hand2")
        update_btn.grid(row=0,column=1)

        #delete btn
        delete_btn = Button(btn_frame,text='DELETE',command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="red",fg="white",cursor="hand2")
        delete_btn.grid(row=0,column=2)

        #reset btn
        reset_btn = Button(btn_frame,text='RESET',command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="red",fg="white",cursor="hand2")
        reset_btn.grid(row=0,column=3)

        #photo frame
        photo_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        photo_frame.place(x=2,y=195,width=690,height=35)


        take_photo_btn = Button(photo_frame,text='TAKE PHOTO SAMPLE',command=self.generate_Dataset,width=35,font=("times new roman",13,"bold"),bg="red",fg="white",cursor="hand2")
        take_photo_btn.grid(row=1,column=0)

        update_btn_photo_btn = Button(photo_frame,text='UPDATE PHOTO SAMPLE',width=35,font=("times new roman",13,"bold"),bg="red",fg="white",cursor="hand2")
        update_btn_photo_btn.grid(row=1,column=1)

        

        #right subframe
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",14,"bold"))
        right_frame.place(x=745,y=10,width=720,height=425)



        #Search System
        Search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",13,"bold"))
        Search_frame.place(x=5,y=10,width=700,height=70)

        Search__lbl = Label(Search_frame,text='Search By:',font=("times new roman",12,"bold"),bg="white")
        Search__lbl.grid(row=0,column=0,padx=10,sticky=W)

        search_comboBox = ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_comboBox["values"]=("Select","StudentID","Phone")
        search_comboBox.current(0)
        search_comboBox.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Search btn
        Search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Search_btn = Button(Search_frame,text='SEARCH',width=12,font=("times new roman",12,"bold"),bg="red",fg="white",cursor="hand2")
        Search_btn.grid(row=0,column=3,padx=4)

        #ShowAll btn
        ShowAll_btn = Button(Search_frame,text='SHOW ALL',width=12,font=("times new roman",12,"bold"),bg="red",fg="white",cursor="hand2")
        ShowAll_btn.grid(row=0,column=4,padx=4)

        #Table Frame
        Table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=95,width=700,height=290)

        #scrollbar
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frame,columns=("deptt","year","semester","studentID","gender","Name","Email","DOB","Phone","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        #pack scroll bar to give side
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #show headers in table
        self.student_table.heading("deptt",text="Department")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("studentID",text="StudentID")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("deptt",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("studentID",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor_data)
        self.fetch_data()
        

#Functions to add data
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_StID=="":
            messagebox.showerror("Error","All Fields are mandatory",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="<your SQL database password>",database="FACE_RECOGNITION_ATTENDANCE_MANAGER")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    self.var_StID.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_name.get(),
                                                                                                    self.var_email.get(),self.var_dob.get(),
                                                                                                    self.var_phone.get(),self.var_radio1.get()


                                                                                                 ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Seccessfull","Student details has been added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)

    #Fetch Data 
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="<your SQL database password>",database="FACE_RECOGNITION_ATTENDANCE_MANAGER")
            my_cursor=conn.cursor()
            my_cursor.execute("select*from student_details")
            data=my_cursor.fetchall()

            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    #get cursor data
    def get_cursor_data(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_year.set(data[1])
        self.var_sem.set(data[2])
        self.var_StID.set(data[3])
        self.var_gender.set(data[4])
        self.var_name.set(data[5])
        self.var_email.set(data[6])
        self.var_dob.set(data[7])
        self.var_phone.set(data[8])
        self.var_radio1.set(data[9])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_StID=="":
            messagebox.showerror("Error","All Fields are mandatory",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="<Your SQL database password>",database="FACE_RECOGNITION_ATTENDANCE_MANAGER")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student_details set Department=%s,Year=%s,Semester=%s,Gender=%s,Name=%s,Email=%s,DOB=%s,Phone=%s,PhotoSample=%s where StudentID=%s",(
                                                                                        self.var_dep.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    
                                                                                                     self.var_gender.get() ,
                                                                                                    
                                                                                                    self.var_name.get(),
                                                                                                    self.var_email.get(),self.var_dob.get(),
                                                                                                    self.var_phone.get(),self.var_radio1.get(),
                                                                                                    self.var_StID.get()
                
                    
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details Updated Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_StID.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete Detail","Do you want to delete",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="<Your SQL database password >",database="FACE_RECOGNITION_ATTENDANCE_MANAGER")
                    my_cursor=conn.cursor()
                    sql="delete from student_details where StudentID=%s"
                    val=(self.var_StID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close
                messagebox.showinfo("Delete","Student details deleted successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    #reset button
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_StID.set("")
        self.var_gender.set("Male")
        self.var_name.set("")
        self.var_email.set("")
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_radio1.set("")



    #Generate Dataset for photo samples
    def generate_Dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_StID=="":
            messagebox.showerror("Error","All Fields are mandatory",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="<Your Sql database password>",database="FACE_RECOGNITION_ATTENDANCE_MANAGER")
                my_cursor=conn.cursor()
                my_cursor.execute("select*from student_details")
                #store date in the variable
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student_details set Department=%s,Year=%s,Semester=%s,Gender=%s,Name=%s,Email=%s,DOB=%s,Phone=%s,PhotoSample=%s where StudentID=%s",(
                                                                                        self.var_dep.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    
                                                                                                     self.var_gender.get() ,
                                                                                                    
                                                                                                    self.var_name.get(),
                                                                                                    self.var_email.get(),self.var_dob.get(),
                                                                                                    self.var_phone.get(),self.var_radio1.get(),
                                                                                                    self.var_StID.get()==id+1
                
                ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #predefined dataset for frontal face from OpenCV
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(grey,1.3,5)
                    #scaling factor=1.3
                    #minimum pinned neighbour=5

                #making rectangle around face
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,My_frame=cap.read()
                    if face_cropped(My_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(My_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Data/std."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==300:
                        break
                cap.release()
                cv2.destroyAllWindows
                messagebox.showinfo("Result","Dataset Generation Completed Successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    













        








        





        




    
    


if __name__ == "__main__":
    root = Tk()
    # Making object of the class
    obj = Student(root)
    root.mainloop()
