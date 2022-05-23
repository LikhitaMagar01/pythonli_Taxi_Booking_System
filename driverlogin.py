############# IMPORTING ALL THE NECESSARY MODULES  ############
from sqlite3.dbapi2 import Cursor, Row
from tkinter import *
import sqlite3
from PIL import Image, ImageTk
from tkinter import messagebox
from driverpage import driverpageClass
######## FOR CONNECTION ##########
import mysql.connector

############### CREATING CLASS ###########
############ DRIVER LOGIN PAGE #########
class driverloginClass():
     def __init__(self):
        self.root=Tk()
        self.root.title("Driver Login Area")
        self.root.geometry("1800x700+0+0")
        self.root.configure(background="yellow")
        
        #frame
        frame_driverlogin=Frame(self.root, bg="white")
        frame_driverlogin.place(x=400, y=150, height=380, width=580)
    
         #image in driver login
        self.bg =ImageTk.PhotoImage(file="loginimage.jpg")
        self.photo_label1=Label(frame_driverlogin, image=self.bg).place(x=0, y=0)
        
        self.Email=StringVar()
        self.Password=StringVar()
    
    #username label and entry
        dri_user_name=Label(frame_driverlogin, text="Email:",font=("goudy old style", 18), bg="white" )
        dri_user_name.place(x=130, y=150, height=30, width=110)
        dri_user_entry=Entry(frame_driverlogin, textvariable=self.Email, font=("times new roman", 14))
        dri_user_entry.place(x=290, y=150, height=30, width=150)
    
    ####### password label and entry
        dri_password=Label(frame_driverlogin, text="Password:",font=("goudy old style", 18), bg="white")
        dri_password.place(x=130, y=200, height=30, width=110)
        dri_pass_entry=Entry(frame_driverlogin, show="*", textvariable=self.Password, font=("times new roman", 14))
        dri_pass_entry.place(x=290, y=200, height=30, width=150)
        
        ##### forget password button
        drilog_Button=Button(frame_driverlogin, text=" forget password? ", font=("goudy old style", 18)).place(x=130, y=250, height=25)
        
        
        #button for login
        drilog_Button=Button(frame_driverlogin, text=" Login ", command=self.drivFunc, font=("goudy old style", 18), height=1, width=7, borderwidth=4)
        drilog_Button.place(x=130, y=300)
        
        ######button for exit
        drilog_Button=Button(frame_driverlogin, text="Exit ", command= exit, font=("goudy old style", 18),height=1, width=7, borderwidth=4)
        drilog_Button.place(x=350, y=300)
        
        ###################   database connection    ####################
     def drivFunc(self):
        con=mysql.connector.connect(host="localhost", user="root",password="root",database="taxibookingsystem")
        cur=con.cursor()
        con.commit()
        if self.Email =="" or self.Password == "":
                messagebox.showerror("error", "all the fields are required", parent=self.root)
        else:
            try:
                cur.execute('SELECT * FROM taxi_driver WHERE email=%s and passwords=%s', (self.Email.get(), self.Password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error", 'INVALID email and password', parent=self.root)
                else:
                    messagebox.showinfo("success", 'welcome, have a safe drive',  parent=self.root)
                    self.root.destroy()
                    self.new_obj=driverpageClass()
                con.close()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)     
       
if __name__=="__main__":         
    obj=driverloginClass()
    mainloop()
