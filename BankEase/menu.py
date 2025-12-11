from models import Admin,Customer
from customerService import customerService
from adminService import adminService

while(1):
    role = int(input("1.Admin 2.Customer 3.Exit\nEnter your option:"))
    if role == 3:
        break
    elif role == 1:
        try:
            username = input("Username:")
            password = input("password:")
            if not adminService.isValid(username,password):
                print("Invalid credentials")
                break
            while(1):
                print("1.register customer\n2.view customer information\n3.update customer details\n4.delete customer\n5.Exit")
                ch = int(input('enter your choice:'))
                if ch == 5:
                    print("Exiting...")
                    break
                elif ch == 1:
                    print("ENTER CUSTOMER DETAILS CAREFULLY!!!")
                    cust = Customer()
                    cust.name = input('name:')
                    cust.mobile_no = input("mobile no.:")
                    cust.email = input("email:")
                    cust.dob = input("date of birth(yyyy-mm-dd):")
                    cust.address = input("Address:")
                    cust.id_proof = input("ID proof number:")
                    cust.acc_type = input("account type(savings/current):")
                    cust.acc_no = adminService.generateAccNo()
                    cust.password = adminService.generateTempPassword()
                    adminService.registerCustomer(cust)
                elif ch == 2:
                    acc_no = int(input("Enter acc_no:"))
                    adminService.viewCustomer(acc_no=acc_no)
                elif ch == 3:
                    acc_no = int(input("Enter acc_no:"))
                    col = input("Enter column to be updated:")
                    if col not in ['name','dob','mobile_no','email','address','id_proof','acc_type']:
                        print("Enter valid column name!!!")
                        continue
                    data = input("enter new data:")
                    adminService.updateCustomerDetails(acc_no=acc_no,col=col,data=data)
                elif ch == 4:
                    acc_no = int(input("Enter acc_no to be deleted:"))
                    adminService.deleteCustomer(acc_no)
                elif ch == 5:
                    break
        except Exception as e:
            print("Error: ",e)
    elif role == 2:
        try:
            acc_no = int(input("Account Number:"))
            password = input("password:")
            if not customerService.isValidCustomer(acc_no,password):
                print("Enter valid credentials...")
                break
            while(1):
                print("----------------DASHBOARD--------------------")
                print("Account Number:",acc_no)
                print("Balance:",customerService.getBalance(acc_no))
                print("Menu")
                print("1.View last 10 transactions\n2.Deposit\n3.Withdraw\n4.Account Closure\n5.Logout")
                ch = int(input("Enter your choice:"))
                if ch == 5:
                    print("Logging out...")
                    break
                elif ch == 1:
                    customerService.viewTransactions(acc_no)
                elif ch == 2:
                    amt = int(input("Enter amount to deposit:"))
                    if amt < 0:
                        print("Amount can't be negative!")
                        continue
                    customerService.deposit(acc_no,amt)
                elif ch == 3:
                    amt = int(input("Enter amount to be withdrawn:"))
                    if amt < 0:
                        print("Amount can't be negative:")
                        continue
                    customerService.withdraw(acc_no,amt)
                elif ch == 4:
                    confirm = input("Are you sure you want to close this account(yes/no):")
                    if not (confirm.lower() == 'yes'):
                        print("going back...")
                        continue
                    bal = customerService.getBalance(acc_no)
                    if bal > 0:
                        print(f"withdraw all existing amount(balance={bal}...)")
                        continue
                    customerService.closeAccount(acc_no)
                    break   

        except Exception as e:
            print("Error: ",e)
    else:
        print("Enter valid option ")
        continue
                    