from one import Account
a=Account("amir",500)
b=Account("ali",200)
a.deposit()
print(a.inventory)
a.transfer(b)
print(a.inventory)
a.withdraw()
print(a.inventory)