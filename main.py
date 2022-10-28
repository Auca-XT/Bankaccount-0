class Bankaccount:
  
  def __init__(self, name, age, balance, deposit, withdraw):
    self.name = name
    self.age = age
    self.balance = balance
    self.deposit = deposit
    self.withdraw = withdraw
      
bc = Bankaccount ("John", 42, float(25000), 500, 250)
  
print(bc.name, "has a bank balance of", '$',bc.balance)
print(bc.name, "deposit $", bc.deposit, "today" '\n')

def balance():
     bc.balance = bc.balance + bc.deposit
  
balance()

print("His bankaccount balance is now $", "\033[32m", bc.balance, "\033[0m")

def newbalance():
  bc.balance = bc.balance - bc.withdraw
  
newbalance()

print("What will his Bankaccount balance be, when he will withdraw", 
"\033[31m", "$250", "\033[0m",'\n')
print("Correct!", bc.name, "has a new balance of $", "\033[32m", bc.balance, "\033[0m")
