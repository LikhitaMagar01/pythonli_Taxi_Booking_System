#########IMPORTING REQUIRED MODULES 
from tkinter import *
import sqlite3
from tkinter import messagebox
from PIL import Image, ImageTk
from register import registerClass
from mainlogin import mainloginClass
############CLASS(OBJECT ORIENTED)#######################
##########    MAKING OF HOMEPAGE  ###################
class homepageClass:
    def __init__(self):
        self.root=Tk()
        self.root.title("online taxi booking system")
        self.root.geometry("1800x700+0+0")
        
        #image
        self.bg=ImageTk.PhotoImage(file="taximainscreen.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=30, y=-30)
        
        #label
        label=Label(self.root, text="welcome to taxi booking system", font=("arial black", 18), foreground="purple")
        label.place(x=500, y= 0)
        label2 = Label(self.root, text="we define your journey", font=("French Script MT", 20), fg="red")
        label2.place(x=610, y=40)

        #buttons
        myButton=Button(self.root, text="Login ", command=self.Log, font=("calibri", 15), padx=36, pady=10, bg="yellow", borderwidth=7)
        myButton.place(x=1000, y=400)
        myButton=Button(self.root, text="Register", command=self.Reg,  font=("calibri", 15), padx=30, pady=10, bg= "yellow", borderwidth=7)
        myButton.place(x=1000, y=500)
        
    ############## FUNCTION TO CONNECT REGISTER BUTTON WITH REGISTERCLASS ################
    def Reg(self):
        self.root.destroy()
        self.new_obj=registerClass()
     ############## FUNCTION TO CONNECT LOGIN BUTTON WITH MAINLOGINCLASS ###########   
    def Log(self):
        self.root.destroy()
        self.new_obj=mainloginClass()
        
        
if __name__=="__main__":        
    obj=homepageClass()
    mainloop()

        
        