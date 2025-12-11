from database import DB
from tabulate import tabulate
from datetime import datetime
import time


crud = DB()

class customerService():
    def __init__(self):
        self.mydb = crud.mydb
        self.cursor = crud.cursor
    def isValidCustomer(self,acc_no,password):
        try:
            self.cursor.execute("select * from customers where acc_no = %s",(acc_no,))
            row = self.cursor.fetchone()
            if (not row) or (row[1] != password):
                print("Inavlid Credentials Entered!!!")
                return False
            print("Logging In....")
            self.cursor.execute("select new_user from customers where acc_no = %s",(acc_no,))
            new_user = self.cursor.fetchone()[0]
            if new_user:
                new_password = input("set new password:")
                new_password1 = input("confirm new password:")
                if new_password != new_password1:
                    print("enter password correctly...")
                    return
                self.cursor.execute("update customers set password = %s where acc_no = %s",(new_password,acc_no))
                self.mydb.commit()
                print("password updated successfully...")
            return True       
        except Exception as e:
            print("Error: ",e)
    def getBalance(self,acc_no):
        try:            
            self.cursor.execute("select balance from customers where acc_no = %s",(acc_no,))
            bal = self.cursor.fetchone()[0]
            return bal
        except Exception as e:
            print("Error: ",e)
    def viewTransactions(self,acc_no):
        try:
            query = "select * from transactions where acc_no = %s order by date_time desc"
            self.cursor.execute(query,(acc_no,))
            rows = self.cursor.fetchmany(10)
            if not rows:
                print("No transactions found!!!")
                return
            print(tabulate(rows,headers=['transaction_id','account_number','type','amount','date_time','balance']))
        except Exception as e:
            print("Error: ",e)
    def deposit(self,acc_no,amt):
        try:
            self.cursor.execute("select acc_no from customers where acc_no = %s",(acc_no,))
            row = self.cursor.fetchone()
            if not row:
                print("No user found...")
                return
            self.cursor.execute("update customers set balance = balance + %s where acc_no = %s",(amt,acc_no))
            self.mydb.commit()
            self.cursor.execute("insert into transactions values(%s,%s,%s,%s,%s,%s)",(self.generate_tid(),acc_no,'deposit',amt,datetime.now()+' ' +time.time(),self.getBalance(acc_no)))
            self.mydb.commit()
            print("Amount deposited successfully...")
        except Exception as e:
            print("Error: ",e)
    def withdraw(self,acc_no,amt):
        try:
            self.cursor.execute("select balance from customers where acc_no = %s",(acc_no,))
            bal = self.cursor.fetchone()[0]
            if bal < amt:
                print("Insufficent Balance...")
                return
            self.cursor.execute("update customers set balance = balance - %s where acc_no = %s",(amt,acc_no))
            self.mydb.commit()
            self.cursor.execute("insert into transactions values(%s,%s,%s,%s,%s,%s)",(self.generate_tid(),acc_no,'withdraw',amt,datetime.now().strftime("%Y-%m-%d/%H-%M-%S"),self.getBalance(acc_no)))
            self.mydb.commit()
            print("Amount withdrawn successfully...")
        except Exception as e:
            print("Error: ",e)
    def closeAccount(self,acc_no):
        try:
            self.cur
            self.cursor.execute("delete from transactions where acc_no = %s",(acc_no,))
            self.cursor.execute("delete from customers where acc_no = %s",(acc_no,))
            self.mydb.commit()
            print("account closed successfully...")
        except Exception as e:
            print("Error: ",e)

    def generate_tid(self):
        date = datetime.now().strftime('%Y%m%d')
        last4 = int(time.time()*1000)
        last4 = str(last4)[-4:]
        return date+last4
