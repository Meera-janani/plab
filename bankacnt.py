class Bank_Account: 
    def __init__(self): 
        self.balance=0
        print("\n\n\tHello!!! Welcome to the Deposit & Withdrawal Machine") 
  
    def deposit(self): 
        amount=float(input("\tEnter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n \tAmount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("\tEnter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n \tYou Withdrew:", amount) 
        else: 
            print("\n \tInsufficient balance  ") 
  
    def display(self): 
        print("\n \tNet Available Balance=",self.balance) 
  
 
s = Bank_Account()  
s.deposit() 
s.withdraw() 
s.display() 
