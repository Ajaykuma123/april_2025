
class ATM():
    def __init__(self,bank_name,branch_name,type,balance):
        self.bank_name= bank_name
        self.branch_name = branch_name
        self.type = type
        self.balance = balance

    def withdraw(self):
        amount =int(input("enter the amount to withdraw: "))
        if amount > self.balance:
            print("Insuffisint funds")
        elif amount <= self.balance and amount >0:
            self.balance -= amount
            print(f"your {amount} is sucessfully withdrawn ")
            print(F"Your current balance is {self.balance}")
        
        

        
              
    

    def change_pin(self):
        current_pin =int(input("enter yor current pin: "))
        if current_pin == pin:
            new_pin = int(input("enter your new pin: "))
            print("your pin is sucessfully changed")
        else:
            print("invalid pin")
            
      
    def transfer(self):
        print("this is transfer")
class ATM_2(ATM):
    def deposit(self):
        print(" this is deposit")
        deposit=float(input("enter the amount to deposit"))
        if deposit > 0 and deposit <= 20000:
            self.balance += deposit
            print(f"this is updated balance {self.balance}")
        else:
            print(f"invalid amount")


    def account_details(self):
        print("this is acount details")
        account_num = int(input("enter your account num: "))
        print(self.bank_name,
              self.branch_name,
              self.type,
              self.balance,account_num)

    
obj = ATM_2("sbi","hyd","savings",0)
# obj.__init__("hdfc","kmr","current",1098)


# pin =int(input("enetr your pin here:"))
               
# if pin>=1000 and pin<=9999:
if True:
    while True:
        print("\n1.withdraw")
        print("2.change your pin")
        print("3.Transfer")
        print("4.deposit")
        print("5.account details")
        choice = int(input("enter your choice: "))
        if choice ==1:
            obj.withdraw()
        elif choice == 2:
            obj.change_pin()
        elif choice == 3:
            obj.transfer()
        elif choice == 4:
            obj.deposit()
        elif choice == 5:
            obj.account_details()
        else:
            print("invalid choice: ")
            break
else:
    print("invalid pin")
    



