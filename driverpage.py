###########  IMPORT MODULES ##########
from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
import mysql.connector
############ CREATE CLASS ###########
####### DRIVER PAGE CREATED #############
class driverpageClass:
    def __init__(self):
        root=Tk()  
        self.root=root
        self.root.title("Driver's system")
        self.root.geometry("1800x700+0+0")
        
        ################ VARIABLE DECLARATION ##############
        self.var_admin_id=StringVar()
        self.var_booking_id=StringVar()
        self.var_customer_name=StringVar()
        self.var_gender=StringVar()
        self.var_booking_date=StringVar()
        self.var_pickup_date=StringVar()
        self.var_pickup_time=StringVar()
        self.var_pickup_address=StringVar()
        self.var_dropoff_date=StringVar()
        self.var_dropoff_destination=StringVar()
        self.var_no_of_car_required=StringVar()
        self.var_driver_name=StringVar()
        self.var_driver_licenes_plate=StringVar()
        
        ##### LABEL 
        label=Label(self.root, text="Get your ride from the list", font=("French Script MT", 20), fg="red").place(x=550, y=40)
        label=Label(self.root, text="drive safely", font=("French Script MT", 20), fg="red").place(x=610, y=80)
        
        #showing details 
        #frame
        frame_view=Frame(self.root, bg="white")
        frame_view.place(x=50, y=150, height=500, width=1200)
        
        #title
        title=Label( frame_view, text="Your Trip Details", font=("impact", 20, "bold"), bg="white")
        title.place(x=120, y=15)  
        
        #scroollbar
        scrolly=Scrollbar(frame_view,orient=VERTICAL)
        scrollx=Scrollbar(frame_view,orient=HORIZONTAL) 
        
        
        #create tables 
        self.admin_Table=ttk.Treeview(frame_view,columns=("admin_id", "bookingconfirmation_id","customer_name", "gender", "booking_date","pickup_date", "pickup_time", "pickup_address", "dropoff_date", "dropoff_destination", "no_of_car_required", "driver_name", "driver_licenes_plate"), yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.admin_Table.xview)
        scrolly.config(command=self.admin_Table.yview)
        
        #heading
        self.admin_Table.heading("admin_id", text="adming ID")
        self.admin_Table.heading("bookingconfirmation_id",text="confirmation ID")
        self.admin_Table.heading("customer_name",text="Customer name")
        self.admin_Table.heading("gender", text="gender")
        self.admin_Table.heading("booking_date",text="Booking date")
        self.admin_Table.heading("pickup_date",text="Pickup date")
        self.admin_Table.heading("pickup_time",text="Pickup time")
        self.admin_Table.heading("pickup_address",text="Pickup address")
        self.admin_Table.heading("dropoff_date",text="Dropoff date")
        self.admin_Table.heading("dropoff_destination",text="Dropoff destination")
        self.admin_Table.heading("no_of_car_required",text="No of cars required")
        self.admin_Table.heading("driver_name", text="driver name")
        self.admin_Table.heading("driver_licenes_plate", text="driver licences plate")

        self.admin_Table["show"]="headings"
        self.admin_Table.column("admin_id", width=100)
        self.admin_Table.column("bookingconfirmation_id",width=100)
        self.admin_Table.column("customer_name",width=100)
        self.admin_Table.column("gender",width=100)
        self.admin_Table.column("booking_date",width=100)
        self.admin_Table.column("pickup_date",width=100)
        self.admin_Table.column("pickup_time",width=100)
        self.admin_Table.column("pickup_address",width=100)
        self.admin_Table.column("dropoff_date",width=100)
        self.admin_Table.column("dropoff_destination",width=100)
        self.admin_Table.column("no_of_car_required",width=100)
        self.admin_Table.column("driver_name", width=100)
        self.admin_Table.column("driver_licenes_plate", width=100)

        self.admin_Table.pack(fill=BOTH,expand=1)
        self.admin_Table.bind("<ButtonRelease-1>",self.get_data)
        self.show() 
        
    def show(self):
        con=mysql.connector.connect(host="localhost", user="root",password="root",database="taxibookingsystem")
        cur=con.cursor()
        try:
            cur.execute("select * from Adminpage")
            rows=cur.fetchall()
            self.admin_Table.delete(*self.admin_Table.get_children())
            for row in rows:
                self.admin_Table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    def get_data(self,ev):
        f=self.admin_Table.focus()
        content=(self.admin_Table.item(f))
        row=content['values']
        self.var_admin_id.set([0]),
        self.var_booking_id.set([1]),
        self.var_customer_name.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_booking_date.set(row[4]),
        self.var_pickup_date.set(row[5]),
        self.var_pickup_time.set(row[6]),
        self.var_pickup_address.set(row[7]),
        self.var_dropoff_date.set(row[8]),
        self.var_dropoff_destination.set(row[9]),
        self.var_no_of_car_required.set(row[10]),
        self.var_driver_name.set(row[11]),
        self.var_driver_licenes_plate.set(row[12])
      
if __name__=="__main__":  
        
    obj=driverpageClass()
    mainloop()