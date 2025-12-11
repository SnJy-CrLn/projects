class Admin():
    def __init__(self,username,password):
        self.username = username
        self.password = password
class Customer():
    def __init__(self,acc_no='',password='',name='',address='',mobile_no='',email='',acc_type='',balance=0,dob='',id_proof='',new_user=True):
       self.acc_no = acc_no
       self.password = password
       self.name = name
       self.address = address
       self.mobile_no = mobile_no
       self.email = email
       self.acc_type = acc_type
       self.balance = balance
       self.dob = dob
       self.id_proof = id_proof
       self.new_user = new_user

'''
Full name
Address
Mobile No
Email id
Type of account-Either Saving Account or Current Account
Initial Balance (min 1000)
Date of Birth
Id proof'''

'''
tid
acc_no
type
amount
date_time
balance
'''