class BankAccount:
 def __init__(self,owner_name,number,balance = 0):
   self.owner_name = owner_name
   self.number = number
   self.transactions = transactions = []
   self.balance = balance
   
 def show_balance(self):
    print(f'Your balance is {self.balance}')


 def deposit(self,amount):
    self.balance += amount
    self.show_balance()
    self.transactions.append(f'Deposit:{amount}')
    return self.balance

 def withdrawls(self,amount):
     self.balance -= amount
     self.show_balance()
     self.transactions.append(f'Deposit:-{amount}')
     return self.balance
 def show_transactions(self):
    for i, track in enumerate(self.transactions):
       print(f'transactio {i+1}:{track}')
  
    
my_account = BankAccount( "Olga Vaisenberg", 156, 100)
my_account.deposit(50)
my_account.withdrawls(25)
print(my_account.balance)
print()
#implemenet those methods , except show_balance , a code that will add their action to the trancaction list and do a deposit and a withdrals and then print the transaction list to track the information
