class Bankaccount:
  
 def __init__(self):
    self.saldo = 999

b = Bankaccount()

print("huidig saldo: ", b.saldo)

class Spaarrekening(Bankaccount):
 def __init__(self):
   print("Spaar rekening wordt gemaakt.")
   self.saldo = 1919
   
s = Spaarrekening()

print("Huidig spaar saldo: ", s.saldo) 

def sparen():
  spaar = 50
  b.saldo = b.saldo - spaar
  s.saldo = s.saldo + spaar
  print("er wordt 50 euro gespaard en bijgeschreven op de spaar rekening", "nieuw saldo ", b.saldo, "spaar saldo", s.saldo, '\n')
  
sparen()  

i = 1
while i < 12:
  sparen()
  i += 1