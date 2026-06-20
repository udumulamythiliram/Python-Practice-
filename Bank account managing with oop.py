class Account:


    def __init__(self,name , money):
        self.name = name
        self.money = money

    def check_balance(self):
        return self.money

    def deposit_money(self,amount):
        if amount < 0:
            print("Amount to be deposited should not be negative!")
            
            if (s:= input("Did you mean withdraw? ( YES OR NO)")).lower()== "yes":
                self.withdraw(-amount)
                
                
        else:
            self.money += amount
            return self.money
        
    def withdraw(self,amount):
        
            if amount < 0:
                print("Amount should not be negative!")

            elif amount > self.money:
                print("Insufficient funds!")

            else:
                self.money -= amount
                return self.money
            

account = Account("mythili",500)
print("Before:",account.check_balance())
account.deposit_money(1000)
account.withdraw(30)
print("After:",account.check_balance())
