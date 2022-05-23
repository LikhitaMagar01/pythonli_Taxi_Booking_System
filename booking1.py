################ IMPORTING REQUIRED MODULES #########
from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from mysql.connector.errors import DatabaseError
############# CLASS CREATED #######
######### BOOKING PAGE MADE ##########
class bookingClass():
    def __init__(self):
        root=Tk()
        self.root=root
        self.root.title("Booking system")
        self.root.geometry("1800x700+0+0")
        
        ######### BUTTON TO BOOK TAXI 
        booking_Button=Button(self.root, text="Book a Taxi ", command=self.book, font=("calibri", 12), padx=52, pady=10,  bg= "light grey", borderwidth=5)
        booking_Button.place(x=30, y=30)
    
        ###### TO VIEW CONFIRMED BOOKING
        view_Button=Button(self.root, text="confirm Bookings ", command=self.viewconfirm, font=("calibri", 12), padx=25, pady=10,  bg= "light grey", borderwidth=5)
        view_Button.place(x=30, y=120)
        #### CANCEL BOOKING
        cancel_Button=Button(self.root, text="cancel my Bookings ", command=self.delete, font=("calibri", 12), padx=15, pady=10,  bg= "light grey", borderwidth=5)
        cancel_Button.place(x=30, y=210)
    ####### LOG OUT BUTTON
        cancel_Button=Button(self.root, text="log out ", command=exit, font=("calibri", 12), padx=20, pady=10,  bg= "light grey", borderwidth=5)
        cancel_Button.place(x=30, y=310)
        
        #frame for booking 
        frame_booking=Frame(self.root, bg="white")
        frame_booking.place(x=240, y=30, height=640, width=480)
        
        ##########VARIABLE DECLARATION #############
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
        self.var_credit_card_number=StringVar()
        self.var_admin_id=StringVar()
        self.var_driver_name=StringVar()
        self.var_driver_licenes_plate=StringVar()
     
        
        #title
        title=Label( frame_booking, text="Booking Page", font=("impact", 20, "bold"), bg="white")
        title.place(x=110, y=10)
        
        #label and entry
        label2=Label( frame_booking, text="Customer name", font=("goudy old style", 18), bg="white").place(x=20, y=90, height=30)
        entry2=Entry( frame_booking, textvariable=self.var_customer_name, font=("calibri", 18),  bg="light grey").place(x=260, y=90, height=30, width=170)
        
        label4=Label( frame_booking, text="Booking date", font=("goudy old style", 18), bg="white").place(x=20, y=130, height=30)
        entry4=Entry( frame_booking, textvariable=self.var_booking_date, font=("calibri", 18), bg="light grey").place(x=260, y=130, height=30, width=170)
        
        label5=Label( frame_booking, text="Pickup date",  font=("goudy old style", 18), bg="white").place(x=20, y=170, height=30)
        entry5=Entry( frame_booking, textvariable=self.var_pickup_date, font=("calibri", 18),  bg="light grey").place(x=260, y=170, height=30, width=170)
        
        label6=Label( frame_booking, text="Pickup_time ", font=("goudy old style", 18), bg="white").place(x=20, y=210, height=30)
        entry6=Entry( frame_booking, textvariable=self.var_pickup_time, font=("calibri", 18), bg="light grey").place(x=260, y=210, height=30, width=170)
        
        label7=Label( frame_booking, text="Pickup_address", font=("goudy old style", 18), bg="white").place(x=20, y=250, height=30)
        entry7=Entry( frame_booking, textvariable=self.var_pickup_address, font=("calibri", 18), bg="light grey").place(x=260, y=250, height=30, width=170)
        
        label8=Label( frame_booking, text="Dropoff_date", font=("goudy old style", 18), bg="white").place(x=20, y=290, height=30)
        entry8=Entry( frame_booking, textvariable=self.var_dropoff_date, font=("calibri", 18), bg="light grey").place(x=260, y=290, height=30, width=170)
        
        label9=Label( frame_booking, text="Dropoff destination", font=("goudy old style", 18), bg="white").place(x=20, y=330, height=30)
        entry9=Entry( frame_booking, textvariable=self.var_dropoff_destination, font=("calibri", 18), bg="light grey").place(x=260, y=330, height=30, width=170)
        
        label10=Label( frame_booking, text="No. of cars required", font=("goudy old style", 18), bg="white").place(x=20, y=370, height=30)
        entry10=Entry( frame_booking, textvariable=self.var_no_of_car_required, font=("calibri", 18), bg="light grey").place(x=260, y=370, height=30, width=170)
        
        label11=Label( frame_booking, text="Creditcard number", font=("goudy old style", 18), bg="white").place(x=20, y=410, height=30)
        entry11=Entry( frame_booking, textvariable=self.var_credit_card_number, font=("calibri", 18), bg="light grey").place(x=260, y=410, height=30, width=170)
        
        clear_Button=Button(frame_booking, text="Clear ", command=self.clear, font=("calibri", 12), padx=20, pady=10,  bg= "light grey", borderwidth=2)
        clear_Button.place(x=130, y=490)
        
        #showing details 
        #frame
        frame_view=Frame(self.root, bg="white")
        frame_view.place(x=760, y=30, height=640, width=560)
        
        #title
        title=Label( frame_view, text="Your Booking Details", font=("impact", 20, "bold"), bg="white")
        title.place(x=120, y=15)  
        
        
        #scroollbar
        scrolly=Scrollbar(frame_view,orient=VERTICAL)
        scrollx=Scrollbar(frame_view,orient=HORIZONTAL) 
        
        
        #create tables 
        self.booking_Table=ttk.Treeview(frame_view,columns=("booking_id","customer_name", "booking_date","pickup_date", "pickup_time", "pickup_address", "dropoff_date", "dropoff_destination", "no_of_car_required", "creditcard_number"), yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.booking_Table.xview)
        scrolly.config(command=self.booking_Table.yview)
        
        self.booking_Table.heading("booking_id",text="booking ID")
        self.booking_Table.heading("customer_name",text="Customer name")
        self.booking_Table.heading("booking_date",text="Booking date")
        self.booking_Table.heading("pickup_date",text="Pickup date")
        self.booking_Table.heading("pickup_time",text="Pickup time")
        self.booking_Table.heading("pickup_address",text="Pickup address")
        self.booking_Table.heading("dropoff_date",text="Dropoff date")
        self.booking_Table.heading("dropoff_destination",text="Dropoff destination")
        self.booking_Table.heading("no_of_car_required",text="No of cars required")
        self.booking_Table.heading("creditcard_number",text="Creditcard number")

        self.booking_Table["show"]="headings"
        self.booking_Table.column("booking_id",width=100)
        self.booking_Table.column("customer_name",width=100)
        self.booking_Table.column("booking_date",width=100)
        self.booking_Table.column("pickup_date",width=100)
        self.booking_Table.column("pickup_time",width=100)
        self.booking_Table.column("pickup_address",width=100)
        self.booking_Table.column("dropoff_date",width=100)
        self.booking_Table.column("dropoff_destination",width=100)
        self.booking_Table.column("no_of_car_required",width=100)
        self.booking_Table.column("creditcard_number",width=100)

        self.booking_Table.pack(fill=BOTH,expand=1)
        self.booking_Table.bind("<ButtonRelease-1>",self.get_data)
        self.show() 
        
        ########showdata
    def show(self):
        con=mysql.connector.connect(host="localhost", user="root",password="root",database="taxibookingsystem")
        cur=con.cursor()
        try:
            cur.execute("select * from Booking")
            rows=cur.fetchall()
            self.booking_Table.delete(*self.booking_Table.get_children())
            for row in rows:
                self.booking_Table.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
          
          ################ TO GET DATAS IN ENTRY  
    def get_data(self,ev):
        f=self.booking_Table.focus()
        content=(self.booking_Table.item(f))
        row=content['values']
        self.var_booking_id.set([0]),
        self.var_customer_name.set(row[1]),
        self.var_booking_date.set(row[2]),
        self.var_pickup_date.set(row[3]),
        self.var_pickup_time.set(row[4]),
        self.var_pickup_address.set(row[5]),
        self.var_dropoff_date.set(row[6]),
        self.var_dropoff_destination.set(row[7]),
        self.var_no_of_car_required.set(row[8]),
        self.var_credit_card_number.set(row[9]),

        ###################book
        ######## DATABASE CONNECTION #################
    def book(self):
        con=mysql.connector.connect(host="localhost", user="root", password="root", database="taxibookingsystem")
        cur=con.cursor()
        cur.execute("INSERT INTO Booking (customer_name, booking_date, pickup_date, pickup_time, pickup_address, dropoff_date, dropoff_destination, no_of_car_required, creditcard_number) values(%s, %s,%s,%s,%s,%s,%s,%s,%s)",
                    (self.var_customer_name.get(),
                     self.var_booking_date.get(),
                     self.var_pickup_date.get(),
                     self.var_pickup_time.get(),
                     self.var_pickup_address.get(),
                     self.var_dropoff_date.get(),
                     self.var_dropoff_destination.get(),
                     self.var_no_of_car_required.get(),
                     self.var_credit_card_number.get()
                    ))
        con.commit()
        messagebox.showinfo("success", "congratulations! booking done successfully", parent=self.root)
        con.close()
        
        
    '''def update(self):
        con=mysql.connector.connect(host="localhost", user="root", password="root", database="taxibookingsystem")
        cur=con.cursor()
        cur.execute("UPDATE Booking SET customer_name=?, booking_date=?, pickup_date=?, pickup_time=?, pickup_address=?, dropoff_date=?, dropoff_destination=?, no_of_car_required=?, creditcard_number=? WHERE booking_id = ?",
                    (
                     self.var_customer_name.get(),
                     self.var_booking_date.get(),
                     self.var_pickup_date.get(),
                     self.var_pickup_time.get(),
                     self.var_pickup_address.get(),
                     self.var_dropoff_date.get(),
                     self.var_dropoff_destination.get(),
                     self.var_no_of_car_required.get(),
                     self.var_credit_card_number.get()
                    ))
        con.commit()
        messagebox.showinfo("success", "your data is updated", parent=self.root)
        con.close()'''
        
        
        ################### DELETE BOOKINGS ##############
    def delete(self):
        con=mysql.connector.connect(host="localhost", user="root",password="root",database="taxibookingsystem")
        cur=con.cursor()
        op=messagebox.askyesno("Confirm", "Do you want to delete?",parent=self.root)
        if op==True:
            cur.execute("delete from Booking where booking_date=?", (self.var_booking_date.get(),))
            con.commit()
            messagebox.showinfo("Delete","booking Deleted Successfully",parent=self.root)
            self.clear()
            self.show()
    
    #################clear
    def clear(self):
        self.var_customer_name.set(""),                                  
        self.var_booking_date.set(""),
        self.var_pickup_date.set(""),
        self.var_pickup_time.set(""),
        self.var_pickup_address.set(""),
        self.var_dropoff_date.set(""),
        self.var_dropoff_destination.set(""),
        self.var_no_of_car_required.set(""),
        self.var_credit_card_number.set("")  
         
         ################ VIEW BOOKING #############
    def viewconfirm(self):
        self.root2=Toplevel()
        self.root2.title("confirm booking")
        self.root2.geometry("1800x800+0+0")
        self.root2.focus_force()
        
        #showing details 
        #frame
        frame_view=Frame(self.root2, bg="white")
        frame_view.place(x=50, y=20, height=500, width=1200)
        
        #title
        title=Label( frame_view, text="Your Confirm Booking Details", font=("impact", 20, "bold"), bg="white")
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
        self.admin_Table.bind("<ButtonRelease-1>",self.get_data1)
        self.show1() 
        
        ############### VIEW CONFIRM BOOKING ############
    def show1(self):
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
            
    def get_data1(self,ev):
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
        
    obj=bookingClass()
    mainloop()