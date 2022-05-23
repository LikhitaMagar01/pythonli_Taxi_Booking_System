################### IMPORTING REQUIRED MODULES###############
from tkinter import *
import sqlite3
from tkinter import messagebox

from customerlogin import customerloginClass
from adminlogin import adminloginClass
from driverlogin import driverloginClass
################ MAKING OF MAIN LOGIN PAGE  ############
class mainloginClass:
    def __init__(self):
        self.root=Tk()
        self.root.title("LOGIN system")
        self.root.geometry("1800x700+0+0")
        self.root.configure(background="grey")
        
        
        
        #frame 
        frame_register=Frame(self.root, bg="white")
        frame_register.place(x=300, y=200, height=300, width=500)
        #title
        title=Label(frame_register, text=" Login as ", font=("impact", 20, "bold"), bg="white")
        title.place(x=170, y=15)
        #fill
        button=Button(frame_register, text="customer", command=self.cuslog, font=("goudy old style", 18), bg="white").place(x=170, y=70, height=30, width=150)
        button=Button(frame_register, text="Driver", command=self.drlog, font=("goudy old style", 18), bg="white").place(x=170, y=120, height=30, width=150)
        button=Button(frame_register, text="Administrator", command=self.adlog, font=("goudy old style", 18), bg="white").place(x=170, y=170, height=30, width=150)
        
    
            
    def cuslog(self):
        self.root.destroy()
        self.new_obj=customerloginClass()
        
    def adlog(self):
        self.root.destroy()
        self.new_obj=adminloginClass()   
    
    def drlog(self):
        self.root.destroy()
        self.new_obj=driverloginClass()
        
    


        
if __name__=="__main__":         
    obj=mainloginClass()
    mainloop()


        