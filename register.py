###############IMPORT REQUIRED MODULES
#FOR TKINTER
from tkinter import *
#THIS IS FOR CONNECTING WITH SQLITE
import sqlite3
#REQUIRED FOR MESSAGE BOX 
from tkinter import messagebox
####FOR CONNECTING TWO PAGES
from mainlogin import mainloginClass
from tkinter import ttk
#####FOR CONNECTING WITH MYSQL WORKBENCH
import mysql.connector

##########CREATE CLASS AND WINDOW CALLED REGISTER SYSTEM
class registerClass():
    def __init__(self):
        self.root=Tk()
        self.root.title("register system")
        self.root.geometry("1800x700+0+0")
        self.root.configure(background="yellow")
        
        
        
        
        ########IMAGE IN REGISTER PAGE
        self.bg=PhotoImage(file="taxi.png")
        self.bg_image=Label(self.root, image=self.bg).place(x=650, y=100)
        
        
        
        ###########EXTRA SERVICES COLUMN############
        label=Label(self.root, text="We provide: ", font=("goudy old style", 18), bg="yellow")
        label.place(x=650, y=450)
        label=Label(self.root, text="-24 Hr service in all the area  ", font=("goudy old style", 18), bg="yellow")
        label.place(x=650, y=480)
        label=Label(self.root, text="-also available for long trips  ", font=("goudy old style", 18), bg="yellow")
        label.place(x=650, y=510)         
        label=Label(self.root, text="-Exciting discount for regular customer  ", font=("goudy old style", 18), bg="yellow")
        label.place(x=650, y=540)
        
    
        
        
        
        ######VARIABLE DECLARATION###############
        self.Firstname=StringVar()
        self.Lastname=StringVar()
        self.Gender=StringVar()
        self.Address=StringVar()
        self.Phonenumber=IntVar()
        self.Email=StringVar()
        self.Creditcardno=IntVar()
        self.Username=StringVar()
        self.Password=StringVar()
        self.Confirmpassword=StringVar()
        self.question=StringVar()
        self.var_chk=IntVar()
        self.securityanswer=StringVar()
        self.cmb_quest=StringVar()
        
        #########FRAME###############
        
        frame_register=Frame(self.root, bg="white")
        frame_register.place(x=10, y=10, height=680, width=600)
        
        ############TITLE####################
        title=Label(frame_register, text="Register Page", font=("impact", 20, "bold"), bg="white")
        title.place(x=200, y=15)
        ##########FIRSTNAME 
        label=Label(frame_register, text="First name", font=("goudy old style", 18), bg="white").place(x=20, y=70, height=30)
        entry=Entry(frame_register, font=("calibri", 18), textvariable=self.Firstname,  bg="light grey").place(x=260, y=70, height=30)
        ##########LAST NAME
        label=Label(frame_register, text="Last name", font=("goudy old style", 18), bg="white").place(x=20, y=110, height=30)
        entry=Entry(frame_register, font=("calibri", 18),textvariable=self.Lastname , bg="light grey").place(x=260, y=110, height=30)
        #########GENDER
        label=Label(frame_register, text="Gender", font=("goudy old style", 18), bg="white").place(x=20, y=150, height=30)
        entry=Entry(frame_register, font=("calibri", 18),textvariable=self.Gender , bg="light grey").place(x=260, y=150, height=30)
        #########ADDRESS
        label=Label(frame_register, text="Address", font=("goudy old style", 18), bg="white").place(x=20, y=190, height=30)
        entry=Entry(frame_register, font=("calibri", 18), textvariable=self.Address,  bg="light grey").place(x=260, y=190, height=30)
        ##########PHONE
        label=Label(frame_register, text="Phone", font=("goudy old style", 18), bg="white").place(x=20, y=230, height=30)
        entry=Entry(frame_register, font=("calibri", 18), textvariable=self.Phonenumber, bg="light grey").place(x=260, y=230, height=30)
        ###########EMAIL
        label=Label(frame_register, text="Email", font=("goudy old style", 18), bg="white").place(x=20, y=270, height=30)
        entry=Entry(frame_register, font=("calibri", 18), textvariable=self.Email, bg="light grey").place(x=260, y=270, height=30)  
        ##########CREDITCARD NUMBER
        label=Label(frame_register, text="CreditCardno", font=("goudy old style", 18), textvariable="Credit", bg="white").place(x=20, y=310, height=30)
        entry=Entry(frame_register, textvariable=self.Creditcardno, font=("calibri", 18), bg="light grey").place(x=260, y=310, height=30)
        ##########USERNAME
        label=Label(frame_register, text="Username", font=("goudy old style", 18), bg="white").place(x=20, y=350, height=30)
        entry=Entry(frame_register, font=("calibri", 18), textvariable=self.Username,bg="light grey").place(x=260, y=350, height=30)
        ###########PASSWORD
        label=Label(frame_register, text="Password", font=("goudy old style", 18), bg="white").place(x=20, y=390, height=30)
        entry=Entry(frame_register, font=("calibri", 18),show="*", textvariable=self.Password,bg="light grey").place(x=260, y=390, height=30)
        ###########CONFIRM PASSWORD
        label=Label(frame_register, text="Confirm Password", font=("goudy old style", 18), bg="white").place(x=20, y=430, height=30)
        entry=Entry(frame_register, font=("calibri", 18), show="*", textvariable=self.Confirmpassword, bg="light grey").place(x=260, y=430, height=30)
        ############SECURITY QUESTION
        question=Label(frame_register, text="Security Question", font=("goudy old style", 18)).place(x=20, y=470, height=30)
        self.cmb_quest=ttk.Combobox(frame_register, font=("goudy old style", 18))
        self.cmb_quest['values']=("Select", "Your First Pet Name", "Your Birthplace", "Your Best Friend Name")
        self.cmb_quest.place(x=20, y=510, height=30)
        self.cmb_quest.current(0)
        ##########ANSWER
        answer=Label(frame_register, text="Answer", font=("goudy old style", 18)).place(x=20, y=550, height=30)
        entry=Entry(frame_register, font=("calibri", 18), textvariable=self.securityanswer, bg="light grey").place(x=260, y=550, height=30)
        
        #########AGREE CHECK BUTTON
        check=Checkbutton(frame_register, onvalue=1, offvalue=0, text="I agree all the terms and conditions regarding this system", variable=self.var_chk ).place(x=20, y=590, height=30)
        
        
        ############REGISTER AND LOGIN BUTTON
        button=Button(frame_register, text="Register", command=self.registerFunc, font=("times new roman", 18, "bold"), bg="yellow").place(x=20, y=630, height=50)
        button=Button(frame_register, text="login", command=self.Log, font=("times new roman", 18, "bold"), bg="yellow").place(x=400, y=630, width= 100, height=50)
        
        
    ###############DATABASE USING SQLITE
        '''#database
        name1=self.Firstname.get()
        name2=self.Lastname.get()
        gender=self.Gender.get()
        address=self.Address.get()
        phonenumber=self.Phonenumber.get()
        email=self.Email.get()
        creditcardno=self.Creditcardno.get()
        username=self.Username.get()
        password=self.Password.get()
        confirmpassword=self.Confirmpassword.get()
    
        conn = sqlite3.connect("taxibooking.db")
        with conn:
            cursor=conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Register(customer_id INT PRIMARY KEY AUTOINCREMENT, Firstname TEXT, Lastname TEXT, Gender TEXT, Address TEXT, Phonenumber int, Email CHARVAR, Credit INT, Username TEXT, Password TEXT, Confirmpassword TEXT)')
            cursor.execute('INSERT INTO Register(Firstname, Lastname, Gender, Address, Phonenumber, Email, Credit, Username, Password, Confirmpassword) values(?,?,?,?,?,?,?,?,?,?)', (name1, name2, gender, address, phonenumber, email, creditcardno, username, password, confirmpassword,))
            conn.commit()'''
            
            
            ################DATABASE USING MYSQL WORKBENCH ####################
                  ################VALIDATION RULES #################
    def registerFunc(self):   

        if self.Password.get()!=self.Confirmpassword.get():
            messagebox.showerror("error", "password and confirm password should be same", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("error", "please agree our terms and condition", parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost", user="root",password="root",database="taxibookingsystem")
                cur=con.cursor()
                cur.execute("INSERT INTO Register ( first_name, last_name, gender, address, phone_number, email, credit_card_no, username, passwords, confirm_passwords, question, security_answer) values( %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s, %s)",
                            (self.Firstname.get(),
                             self.Lastname.get(),
                             self.Gender.get(),
                             self.Address.get(),
                             self.Phonenumber.get(),
                             self.Email.get(),
                             self.Creditcardno.get(),
                             self.Username.get(),
                             self.Password.get(),
                             self.Confirmpassword.get(),
                             self.cmb_quest.get(),
                             self.securityanswer.get()
                            ))
                con.commit()
                con.close()
                messagebox.showinfo("success", "registered successfully", parent=self.root)
                self.clearFunc()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
                
        
                
    def clearFunc(self):
        self.Firstname.set(""),
        self.Lastname.set(""),
        self.Gender.set(""),
        self.Address.set(""),
        self.Phonenumber.set(""),
        self.Email.set(""),
        self.Creditcardno.set(""),
        self.Username.set(""),
        self.Password.set(""),
        self.Confirmpassword.set(""),
        self.securityanswer.Set("")
                
            
            
            
            

        
    def Log(self):
        self.root.destroy()
        self.new_obj=mainloginClass()
                
           
        
if __name__=="__main__":         
    obj=registerClass()
    mainloop()
