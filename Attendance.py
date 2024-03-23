from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root

# Set geometry of window
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendy-Pro")

        #text variables
        self.atten_id=StringVar()
        self.atten_name=StringVar()
        self.atten_dep=StringVar()
        self.atten_time=StringVar()
        self.atten_date=StringVar()
        self.status=StringVar()

        img=Image.open("GUI images/atty1.PNG")
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

        #main frame
        main_frame=Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=20,y=18,width=1480,height=600)

         #left subframe
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Information",font=("times new roman",14,"bold"))
        left_frame.place(x=10,y=10,width=720,height=455)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y=18,width=697,height=400)

        #label entry
        #attendance id label
        attendance_id_lbl = Label(left_inside_frame,text='AttendanceID:',font=("times new roman",20,"bold"),bg="white")
        attendance_id_lbl.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        AttendanceID_entry=ttk.Entry(left_inside_frame,textvariable=self.atten_id,width=10,font=("times new roman",20,"bold"))
        AttendanceID_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #student name
        student_name_lbl = Label(left_inside_frame,text='Name:',font=("times new roman",20,"bold"),bg="white")
        student_name_lbl.grid(row=1,column=0,padx=10,sticky=W)
        StudentName_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.atten_name,font=("times new roman",20,"bold"))
        StudentName_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #student dep
        Dep_lbl = Label(left_inside_frame,text='Department:',font=("times new roman",20,"bold"),bg="white")
        Dep_lbl.grid(row=2,column=0,padx=10,sticky=W)
        Dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.atten_dep,font=("times new roman",20,"bold"))
        Dep_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #date
        date_lbl = Label(left_inside_frame,text='Date:',font=("times new roman",20,"bold"),bg="white")
        date_lbl.grid(row=3,column=0,padx=10,sticky=W)
        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.atten_date,font=("times new roman",20,"bold"))
        date_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

         #time
        time_lbl = Label(left_inside_frame,text='Time:',font=("times new roman",20,"bold"),bg="white")
        time_lbl.grid(row=4,column=0,padx=10,sticky=W)
        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.atten_time,font=("times new roman",20,"bold"))
        time_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        #attendance status
        status_lbl = Label(left_inside_frame,text='Attendance Status:',font=("times new roman",20,"bold"),bg="white")
        status_lbl.grid(row=5,column=0,padx=10,sticky=W)

        Status = ttk.Combobox(left_inside_frame,textvariable=self.status,font=("times new roman",20,"bold"),width=17,state="readonly")
        Status["values"]=("Status","Present","Absent")
        Status.current(0)
        Status.grid(row=5,column=1,padx=10,pady=10,sticky=W)

        #frame for buttons
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=354,width=690,height=35)

        #save button
        save_btn = Button(btn_frame,text='IMPORT CSV',command=self.importCSV,width=17,font=("times new roman",13,"bold"),bg="red",fg="white",cursor="hand2")
        save_btn.grid(row=0,column=0)

        #update button
        update_btn = Button(btn_frame,text='EXPORT CSV',command=self.exportcsv,width=17,font=("times new roman",13,"bold"),bg="red",fg="white",cursor="hand2")
        update_btn.grid(row=0,column=1)

        #delete btn
        delete_btn = Button(btn_frame,text='DELETE',width=17,font=("times new roman",13,"bold"),bg="red",fg="white",cursor="hand2")
        delete_btn.grid(row=0,column=2)

        #reset btn
        reset_btn = Button(btn_frame,text='RESET',command=self.reset,width=17,font=("times new roman",13,"bold"),bg="red",fg="white",cursor="hand2")
        reset_btn.grid(row=0,column=3)



        

        #right subframe
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",14,"bold"))
        right_frame.place(x=745,y=10,width=720,height=455)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=18,width=697,height=400)

        #Scroll Bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        #attendance report table
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","Name","Department","Date","Time","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("Name",text="Name of Student")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Status",text="Status")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Status",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_field)

##############FETCH DATA#######################
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCSV(self):
        global mydata
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    
    def get_field(self,event=""):
        field_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(field_row)
        rows=content['values']
        self.atten_id.set(rows[0])
        self.atten_name.set(rows[1])
        self.atten_dep.set(rows[2])
        self.atten_date.set(rows[3])
        self.atten_time.set(rows[4])
        self.status.set(rows[5])

    def reset(self):
        self.atten_id.set("")
        self.atten_name.set("")
        self.atten_dep.set("")
        self.atten_date.set("")
        self.atten_time.set("")
        self.status.set("")


    


        








            








if __name__ == "__main__":
    root = Tk()
    # Making object of the class
    obj = Attendance(root)
    root.mainloop()
