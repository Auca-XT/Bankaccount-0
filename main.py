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

bc.balance = bc.balance + bc.deposit

print("His bankaccount balance is now $", bc.balance)

bc.balance = bc.balance - bc.withdraw

print("What will his Bankaccount balance be, when he will withdraw", "$ 250", '\n')
print("Correct ", bc.name, "has a new balance of $", bc.balance)