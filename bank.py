class Bank :
    def __init__(self,name,branch,account_no,balance) :
        self.name = name 
        self.branch = branch
        self.account_no = account_no
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self , amount):
        if self.balance >= amount :
            self.balance -= amount
        else :
            print("ineffiecient balance")
    def display(self):
        print("\n name :",self.name)
        print("\n branch :",self.branch)
        print("\n account no :",self.account_no)
        print("\n balance  :",self.balance)

account = Bank("fasil","chithara",56789,1000)
while(1):
    print("\n 1.deposit")
    print("\n 2.withdraw")
    print("\n 3.display")
    print("\n 4.exit")
    c = int(input("\n enter choice:"))
    match(c) :
        case 1 :
            amount = int(input("\n enter amount to deposit:"))
            account.deposit(amount)
        case 2 :
            amount = int(input("\n enter amount to withdraw:"))
            account.withdraw(amount)
        case 3 :
            account.display()
        case 4 :
            break
        case _ :
            print("\n invalid choice")
            

        