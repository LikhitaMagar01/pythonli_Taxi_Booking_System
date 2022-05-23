############## MODULES IMPORTED ########
from tkinter import *
import sqlite3
from tkinter import ttk, messagebox
import mysql.connector
######### CLASS CREATED ####
##### ADMIN PAGE CREATED #############
class adminpageClass:
    def __init__(self):
        root=Tk()  
        self.root=root
        self.root.title("Booking Confirmation system")
        self.root.geometry("1800x700+0+0")
        
        #frame 
        frame_admin=Frame(self.root, bg="white")
        frame_admin.place(x=50, y=30, height=640, width=480)
        
        #title
        title=Label( frame_admin, text="admin Page", font=("impact", 20, "bold"), bg="white")
        title.place(x=110, y=0)
        
        #########VARIABLE DECLARATION
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
        
        #fill LABEL AND ENTRY 
        label1=Label( frame_admin, text="Confirmation ID", font=("goudy old style", 18), bg="white").place(x=20, y=30, height=30)
        entry1=Entry( frame_admin, textvariable=self.var_booking_id, font=("calibri", 18),  bg="light grey").place(x=260, y=30, height=30, width=170)

        label2=Label( frame_admin, text="Customer name", font=("goudy old style", 18), bg="white").place(x=20, y=70, height=30)
        entry2=Entry( frame_admin, textvariable=self.var_customer_name, font=("calibri", 18),  bg="light grey").place(x=260, y=70, height=30, width=170)
        
        label3=Label( frame_admin, text="Gender", font=("goudy old style", 18), bg="white").place(x=20, y=110, height=30)
        entry3=Entry(frame_admin, textvariable=self.var_gender, font=("calibri", 18), bg="light grey").place(x=260, y=110, height=30, width=170)
        
        label4=Label(frame_admin, text="Booking date", font=("goudy old style", 18), bg="white").place(x=20, y=150, height=30)
        entry4=Entry(frame_admin, textvariable=self.var_booking_date, font=("calibri", 18), bg="light grey").place(x=260, y=150, height=30, width=170)
        
        label5=Label(frame_admin, text="Pickup date",  font=("goudy old style", 18), bg="white").place(x=20, y=190, height=30)
        entry5=Entry(frame_admin, textvariable=self.var_pickup_date, font=("calibri", 18),  bg="light grey").place(x=260, y=190, height=30, width=170)
        
        label6=Label(frame_admin, text="Pickup time ", font=("goudy old style", 18), bg="white").place(x=20, y=230, height=30)
        entry6=Entry(frame_admin, textvariable=self.var_pickup_time, font=("calibri", 18), bg="light grey").place(x=260, y=230, height=30, width=170)
        
        label7=Label(frame_admin, text="Pickup address", font=("goudy old style", 18), bg="white").place(x=20, y=270, height=30)
        entry7=Entry(frame_admin, textvariable=self.var_pickup_address, font=("calibri", 18), bg="light grey").place(x=260, y=270, height=30, width=170)
        
        label8=Label(frame_admin, text="Dropoff date", font=("goudy old style", 18), bg="white").place(x=20, y=310, height=30)
        entry8=Entry(frame_admin, textvariable=self.var_dropoff_date, font=("calibri", 18), bg="light grey").place(x=260, y=310, height=30, width=170)
        
        label9=Label(frame_admin, text="Dropoff destination", font=("goudy old style", 18), bg="white").place(x=20, y=350, height=30)
        entry9=Entry(frame_admin, textvariable=self.var_dropoff_destination, font=("calibri", 18), bg="light grey").place(x=260, y=350, height=30, width=170)
        
        label10=Label(frame_admin, text="No. of cars required", font=("goudy old style", 18), bg="white").place(x=20, y=390, height=30)
        entry10=Entry(frame_admin, textvariable=self.var_no_of_car_required, font=("calibri", 18), bg="light grey").place(x=260, y=390, height=30, width=170)
        
        label10=Label(frame_admin, text="Driver's name", font=("goudy old style", 18), bg="white").place(x=20, y=440, height=30)
        entry10=Entry(frame_admin, textvariable=self.var_driver_name, font=("calibri", 18), bg="light grey").place(x=260, y=440, height=30, width=170)
        
        label10=Label(frame_admin, text="Driver's licences plate", font=("goudy old style", 18), bg="white").place(x=20, y=480, height=30)
        entry10=Entry(frame_admin, textvariable=self.var_driver_licenes_plate, font=("calibri", 18), bg="light grey").place(x=260, y=480, height=30, width=170)
        
        btnconfirm=Button(frame_admin, text= "confirm", command=self.confirm, font=("calibri", 18), bg="light grey").place(x=15, y=530, height=30, width=100)
        btn=Button(frame_admin, text= "clear", command=self.clear, font=("calibri", 18), bg="light grey").place(x=310, y=530, height=30, width=100)
        
        ###########BILLING BUTTON
        btn=Button(frame_admin, text= "Bill", command=self.bill, font=("calibri", 18), bg="light grey").place(x=150, y=530, height=30, width=100)
        
       #showing details 
        #frame
        frame_view=Frame(self.root, bg="white")
        frame_view.place(x=550, y=30, height=640, width=800)
        
        #title
        title=Label( frame_view, text="Your Booking Details", font=("impact", 20, "bold"), bg="white")
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
        
        ############## SHOW CONFIRMATION PAGE ################
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
        
    def clear(self):
        self.var_booking_id.set(""),   
        self.var_customer_name.set("",)  
        self.var_gender.set(""),                 
        self.var_booking_date.set(""),
        self.var_pickup_date.set(""),
        self.var_pickup_time.set(""),
        self.var_pickup_address.set(""),
        self.var_dropoff_date.set(""),
        self.var_dropoff_destination.set(""),
        self.var_no_of_car_required.set(""),
        self.var_driver_name.set(""),
        self.var_driver_licenes_plate.set("")
        
        
        #######################database
    def confirm(self):
        con=mysql.connector.connect(host="localhost", user="root", password="root", database="taxibookingsystem")
        cur=con.cursor()
        cur.execute("INSERT INTO Adminpage (bookingconfirmation_id, customer_name, gender, booking_date, pickup_date, pickup_time, pickup_address, dropoff_date, dropoff_destination, no_of_car_required, driver_name, driver_licenes_plate) values(%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (self.var_booking_id.get(),
                     self.var_customer_name.get(),
                     self.var_gender.get(),
                     self.var_booking_date.get(),
                     self.var_pickup_date.get(),
                     self.var_pickup_time.get(),
                     self.var_pickup_address.get(),
                     self.var_dropoff_date.get(),
                     self.var_dropoff_destination.get(),
                     self.var_no_of_car_required.get(),
                     self.var_driver_name.get(),
                     self.var_driver_licenes_plate.get()
                    ))
        con.commit()
        messagebox.showinfo("success", "congratulations! booking confirmed successfully", parent=self.root)
        con.close()
        
        #frame
        frame_view=Frame(self.root, bg="white")
        frame_view.place(x=560, y=30, height=640, width=770)


##################### FOR BILLING #############################
    def bill(self):
        self.root=Toplevel()
        self.root.title("Billing Area")
        self.root.geometry("700x630+600+10")
        self.root.config(bg="pink")
        
        self.distance=StringVar()
        self.amount=IntVar()
        self.total=IntVar()
        self.name=StringVar()
        
        
        label1=Label(self.root, text="billing area per travel", bg="pink", font=("goudy old style", 18)).place(x=150, y=10)
        
        label1=Label(self.root, text="customer name", bg="pink", font=("goudy old style", 18)).place(x=50, y=50)
        entry1=Entry(self.root, textvariable=self.name, font=("times new roman", 14)).place(x=300, y=50)
        
        label1=Label(self.root, text="total miles travelled", bg="pink", font=("goudy old style", 18)).place(x=50, y=100)
        entry1=Entry(self.root, textvariable=self.distance, font=("times new roman", 14)).place(x=300, y=100)
        
        label2=Label(self.root, text="amt per miles", bg="pink", font=("goudy old style", 18)).place(x=50, y=150)
        entry2=Entry(self.root, textvariable=self.amount, font=("times new roman", 14)).place(x=300, y=150)
        
        btn=Button(self.root, command=self.multiply, text="multiply").place(x=300, y=200)
        
        
        label1=Label(self.root, text="total in $", bg="pink", font=("goudy old style", 18)).place(x=50, y=250)
        entry3=Entry(self.root, textvariable=self.total, font=("times new roman", 14)).place(x=300, y=250)
        
        label1=Label(self.root, text="your total amount for this trip is(in $) ", bg="pink", font=("goudy old style", 18)).place(x=50, y=300)
        entry3=Entry(self.root, textvariable=self.total, font=("times new roman", 14)).place(x=410, y=300, width=60)
        
        
        
                        
    def multiply(self):
         
         a=int(self.distance.get())
         b=int(self.amount.get())
         total=a*b
         self.total.set(str(total))
         con=mysql.connector.connect(host="localhost", user="root", password="root", database="taxibookingsystem")
         cur=con.cursor()
         cur.execute("INSERT INTO Billing (customer_name, distance_travelled, amount_per_miles, total ) values(%s, %s,%s,%s)",
                    (self.name.get(),
                     self.distance.get(),
                     self.amount.get(),
                     self.total.get()
                    ))
         con.commit()
         messagebox.showinfo("success", "billing is made", parent=self.root)
         con.close()

      
if __name__=="__main__":    
        
    obj=adminpageClass()
    mainloop()