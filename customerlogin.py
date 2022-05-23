
#############CUSTOMER LOGIN PAGE WIHT TKINGER ###############

#############IMPORTING ALL THE REQUIRED MODULES
from logging import exception
from tkinter import *
###########FOR IMPORTING IMAGE
from PIL import Image, ImageTk
##########FOR IMPORTING MESSAGE BOX
from tkinter import messagebox
##########FOR ttk COMBOBOX
from tkinter import ttk
#########FOR IMPORTING AND CONNECTING WITH BOOKINGCLASS PAGE 
from booking1 import bookingClass
##########FOR CONNECTING WITH MYSQL WORKBENCH
import mysql.connector

##########CREATING CLASS CUSTOMERLOGINCLASS AND CUSTOMER LOIGN PAGE 
class customerloginClass():
     def __init__(self):
        self.root=Tk()
        self.root.title("Customer Login Area")
        self.root.geometry("1800x700+0+0")
        self.root.configure(background="yellow")
        
       
        
        
        ##############FRAME IN THE PAGE FOR LOGIN
        frame_customerlogin=Frame(self.root, bg="white")
        frame_customerlogin.place(x=400, y=150, height=380, width=580)
    
         ###############IMAGE IN LOGIN FRAME
        self.bg =ImageTk.PhotoImage(file="loginimage.jpg")
        self.photo_label1=Label(frame_customerlogin, image=self.bg).place(x=0, y=0)
        
        ############VARIABLE DECLARATION
        self.Email=StringVar()
        self.Password=StringVar()
        self.securityanswer=StringVar()
        self.newpassword=StringVar()
    
    
    
        ################  USERNAME 
        cus_user_name=Label(frame_customerlogin, text="Email:",font=("goudy old style", 18), bg="white" )
        cus_user_name.place(x=130, y=150, height=30)
        cus_user_entry=Entry(frame_customerlogin, textvariable=self.Email, font=("times new roman", 16))
        cus_user_entry.place(x=290, y=150, height=30, width=150)
        
        #############  PASSWORD
        cus_password=Label(frame_customerlogin, text="Password:",font=("goudy old style", 18), bg="white")
        cus_password.place(x=130, y=200, height=30, width=110)
        cus_pass_entry=Entry(frame_customerlogin, show="*", textvariable=self.Password, font=("times new roman", 16))
        cus_pass_entry.place(x=290, y=200, height=30, width=150)
        
        ##############FORGET PASSWORD
        cuslog_Button=Button(frame_customerlogin, command=self.forget, text=" forget password? ", font=("goudy old style", 18)).place(x=130, y=250, height=25)
        
        
        ############# BUTTON FOR LOGIN
        cuslog_Button=Button(frame_customerlogin, text=" Login ", command=self.cusloginFunc, font=("goudy old style", 18), height=1, width=7, borderwidth=4)
        cuslog_Button.place(x=130, y=300)
        
        ############ BUTTON FOR EXIT
        cuslog_Button=Button(frame_customerlogin, text="Exit ", command= exit, font=("goudy old style", 18),height=1, width=7, borderwidth=4)
        cuslog_Button.place(x=350, y=300)
        
        
        ############ DATABASE FOR CONNECTION WITH MYSQL WITH VALIDATION 
     def cusloginFunc(self):
        #database
        
        con=mysql.connector.connect(host="localhost", user="root",password="root",database="taxibookingsystem")
        cur=con.cursor()
        con.commit()
        if self.Email =="" or self.Password == "":
                messagebox.showerror("error", "all the fields are required", parent=self.root)
        else:
            try:
                cur.execute('SELECT * FROM register WHERE Email=%s and Passwords=%s', (self.Email.get(), self.Password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error", 'INVALID email and password', parent=self.root)
                else:
                    messagebox.showinfo("success", 'welcome to booking area',  parent=self.root)
                    self.root.destroy()
                    self.new_obj=bookingClass()
                con.close()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
                    
                    
     '''def book(self):
        self.root.destroy()
        self.new_obj=bookingClass()  '''  
        
        #################### RESET PASSWORD #######################
     def resetpassword(self):
        con=mysql.connector.connect(host="localhost", user="root",password="root",database="taxibookingsystem")
        cur=con.cursor()
        con.commit()
        if self.cmb_quest=="Select" or self.securityanswer=="" or self.newpassword=="":
            messagebox.showerror("error", "all the field are required to reset the new password", parent=self.root)
        else:
            try:
                cur.execute("SELECT * FROM register WHERE Email=%s and question=%s and security_answer=%s", (self.Email.get(), self.cmb_quest.get(), self.securityanswer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error", "enter valid security question and answer", parent=self.root)
                else:
                    cur.execute("UPDATE register SET passwords=%s where Email=%s", (self.newpassword.get(), self.Email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("success", "your password is reset", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
        
        
        ############## FOR FORGET PASSWORD PAGE    
     def forget(self):
        con=mysql.connector.connect(host="localhost", user="root",password="root",database="taxibookingsystem")
        cur=con.cursor()
        con.commit()
        if self.Email.get() =="":
            messagebox.showerror("error", "enter your email to reset the password", parent=self.root)
        else:
            try:
                cur.execute("SELECT * FROM register WHERE Email=%s", (self.Email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error", "enter valid email", parent=self.root)
                else:
                    self.root2=Toplevel()
                    self.root2.title("forget password")
                    self.root2.geometry("400x350+490+180")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
         
                    t=Label(self.root2, text="forget password", font=("times new roman", 20, "bold"), fg="red", bg="white").place(x=90, y=20)
         
                     ############SECURITY QUESTION
                    question=Label(self.root2, text="Security Question", font=("goudy old style", 18)).place(x=10, y=60, height=30)
                    self.cmb_quest=ttk.Combobox(self.root2, font=("goudy old style", 18))
                    self.cmb_quest['values']=("Select", "Your First Pet Name", "Your Birthplace", "Your Best Friend Name")
                    self.cmb_quest.place(x=10, y=100, height=30)
                    self.cmb_quest.current(0)
                      ##########ANSWER
                    answer=Label(self.root2, text="Answer", font=("goudy old style", 18)).place(x=10, y=140, height=30)
                    entry=Entry(self.root2, font=("calibri", 18), textvariable=self.securityanswer, bg="light grey").place(x=170, y=140, height=30, width=210)
                     ##########NEW PASSWORD 
                    label=Label(self.root2, text="New password", font=("goudy old style", 15), bg="white").place(x=10, y=200, height=30)
                    entry=Entry(self.root2, textvariable=self.newpassword, font=("calibri", 15), bg="light grey").place(x=170, y=190, height=30, width=210)
                     ############ PASSWORD SETUP BUTTON
                    change_Button=Button(self.root2, text="reset password ", command=self.resetpassword, font=("goudy old style", 18),height=1, width=15, borderwidth=4, bg="red").place(x=100, y=240)
            
                con.close()
                
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
                    
         
                    
             
    
        
if __name__=="__main__":         
    obj=customerloginClass()
    mainloop()
