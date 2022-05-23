
############  IMPORTING REQUIRED MODULES ###############
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from adminpage1 import adminpageClass
###########  CREATING CLASS ############
########## CREATING ADMIN LOGIN PAGE ########
class adminloginClass():
     def __init__(self):
        self.root=Tk()
        self.root.title("Administration Login Area")
        self.root.geometry("1800x700+0+0")
        self.root.configure(background="yellow")
        
        #frame
        frame_adminlogin=Frame(self.root, bg="white")
        frame_adminlogin.place(x=400, y=150, height=380, width=580)
        
    
         #image in admin login
        self.bg =ImageTk.PhotoImage(file="loginimage.jpg")
        self.photo_label1=Label(frame_adminlogin, image=self.bg).place(x=0, y=0)
        
        ####VARIABLE DECLARATION
        self.Email=StringVar()
        self.Password=StringVar()
    
    
    
    #username and password label and entry
        ad_email=Label(frame_adminlogin, text="Email:",font=("goudy old style", 18), bg="white" )
        ad_email.place(x=130, y=150, height=30)
        ad_email_entry=Entry(frame_adminlogin, textvariable=self.Email, font=("times new roman", 16))
        ad_email_entry.place(x=290, y=150, height=30, width=150)
    
        cus_password=Label(frame_adminlogin, text="Password:",font=("goudy old style", 18), bg="white")
        cus_password.place(x=130, y=200, height=30, width=110)
        cus_pass_entry=Entry(frame_adminlogin, show="*", textvariable=self.Password, font=("times new roman", 16))
        cus_pass_entry.place(x=290, y=200, height=30, width=150)
        
        cuslog_Button=Button(frame_adminlogin, text=" forget password? ", font=("goudy old style", 18)).place(x=130, y=250, height=25)
        
        
        #button
        cuslog_Button=Button(frame_adminlogin, text=" Login ", command=self.adminloginFunc, font=("goudy old style", 18), height=1, width=7, borderwidth=4)
        cuslog_Button.place(x=130, y=300)
        cuslog_Button=Button(frame_adminlogin, text="Exit ", command= exit, font=("goudy old style", 18),height=1, width=7, borderwidth=4)
        cuslog_Button.place(x=350, y=300)
        
     #database
     def adminloginFunc(self):
        
        #database
        
        con=mysql.connector.connect(host="localhost", user="root",password="root",database="taxibookingsystem")
        cur=con.cursor()
        con.commit()
        if self.Email =="" or self.Password == "":
                messagebox.showerror("error", "all the fields are required", parent=self.root)
        else:
            try:
                cur.execute('SELECT * FROM Co_staff WHERE staff_email = %s and passwords = %s', (self.Email.get(), self.Password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error", 'INVALID email and password', parent=self.root)
                else:
                    messagebox.showinfo("success", 'welcome to admin area',  parent=self.root)
                    self.root.destroy()
                    self.new_object=adminpageClass()
                con.close()
                
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
                       
        
       
if __name__=="__main__":         
    obj=adminloginClass()
    mainloop()
