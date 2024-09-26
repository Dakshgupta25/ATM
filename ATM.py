def check_password():
    global password
    
    passw=input("enter your password: ")
    if passw==password:
        print("press 1 for balance ")
        print("press 2 for credit ")
        print("press 3 for debit ")
        print("press 4 for change password ")
        print("press anykey to exit ")
        choice=int(input("enter your choice: "))
        if choice==1:
            check_balance()
        elif choice==2:
            credit()
        elif choice==3:
            debit()
        elif choice==4:
            change_pass()
        else:
            print("thankyou")
    else:
        print("password is incorrect")

def my_balance():
    global balance
    global password
    balance=10000
    password="1234"
def check_balance():
    global balance
    print("your balance is :",balance)
def credit():
    global balance
    amount=int(input("enter the amount"))
    balance = balance+amount
    check_balance()
def debit():
    global balance
    amount=int(input("enter the amount you wanna debit"))
    if amount>balance:
        print("insufficent balance")
    else:
        balance=balance-amount
        check_balance()
def change_pass():
    global password
    oldpass=input("enter current pass: ")
    if oldpass==password:
        password=input("enter new password: ")
        print("your current password is", password)
    else:
        print("enter the correct password")
        
my_balance()
check_password()
a=int(input("press 0 to continue: "))
i=0
while i<1:
    if a == 0:
       check_password()
    else:
        print("exited")
    a=int(input("press 0 to continue: "))
    i=a
