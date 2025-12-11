from database import DB
from datetime import datetime
import time
import string
import random
from tabulate import tabulate
crud = DB()

class adminService():
    def __init__(self):
        self.mydb = crud.mydb
        self.cursor = crud.cursor
    def isValid(self,username,password):
        try:
            self.cursor.execute("select * from admins where username = %s",(username,))
            row = self.cursor.fetchone()
            if (not row) or (row[1] != password):
                print("Inavlid Admin Credentials Entered!!!")
                return False
            print("Logging In....")
            return True
        except Exception as e:
            print("Error: ",e)
    def registerCustomer(self,customer):
        try:
            query = "insert into customers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(query,(customer.acc_no,customer.password,customer.name,customer.address,customer.mobile_no,customer.email,customer.acc_type,customer.balance,customer.dob,customer.id_proof,customer.new_user))
            self.mydb.commit()
            print("Customer Registered Successfully!!!")
        except Exception as e:
            print("Error: ",e)
    def viewCustomer(self,acc_no):
        try:
            self.cursor.execute("select acc_no,name,dob,mobile_no,email,address,id_proof,acc_type from customers where acc_no = %s",(acc_no,))
            row = self.cursor.fetchone()
            if not row:
                print("No such user is present...")
                return
            print(tabulate([row],headers=['acc_no','name','dob','mobile_no','email','address','id_proof','acc_type'],tablefmt='fancy_grid'))
        except Exception as e:
            print("Error: ",e)    
    def deleteCustomer(self,acc_no):
        try:
            self.cursor.execute("select acc_no from customers where acc_no=%s",(acc_no,))
            row = self.cursor.fetchone()
            if not row:
                print("No such user found!!!")
                return
            self.cursor.execute("delete from customers where acc_no = %s",(acc_no,))
            self.mydb.commit()
            print("customer deleted successfully...")
        except Exception as e:
            print("Error: ",e)
    def updateCustomerDetails(self,acc_no,col,data):
        try:
            self.cursor.execute("select acc_no from customers where acc_no=%s",(acc_no,))
            row = self.cursor.fetchone()
            if not row:
                print("No such user found!!!")
                return
            self.cursor.execute(f"update customers set {col} = %s where acc_no = %s",(data,acc_no))
            self.mydb.commit()
            print("details updated...")
        except Exception as e:
            print("Error: ",e)

                

    def generateAccNo(self):
        date = datetime.now().strftime('%Y%m%d')
        last4 = int(time.time()*1000)
        last4 = str(last4)[-4:]
        return date+last4
    def generateTempPassword(self):
        char = string.ascii_letters + string.digits
        temp = ''
        for _ in range(8):
            temp += random.choice(char)
        return temp
    