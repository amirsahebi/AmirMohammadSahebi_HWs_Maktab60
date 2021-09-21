import datetime
class Account:
    # defining a amount for minimum of inventory
    min_inventory=5
    def __init__(self,name,inventory):
        self.name=name
        self.inventory=int(inventory)
        self.transactions=[]

    # defining a method for depositing from account
    def deposit(self):
        add=int(input("Please enter the amount:"))
        self.inventory += add
        # appending transactions' details to the list
        self.transactions.append({"type":"deposit","amount":add,"date&time":datetime.datetime.today().strftime("%m/%d/%y,%H:%M")})
    
    # defining a method for withdraw from account
    def withdraw(self):
        reduce=int(input("Please enter the amount:"))
        if self.check_inventory(reduce):
            self.inventory -= reduce
        # appending transactions' details to the list
        self.transactions.append({"type":"withdraw","amount":reduce,"date&time":datetime.datetime.today().strftime("%m/%d/%y,%H:%M")})

    # defining a method for transfer to another account
    def transfer(self,account):
        move=int(input("Please enter the amount:"))
        if self.check_inventory(move):
            self.inventory -= move
            account.inventory += move
        # appending transactions' details to the list
        self.transactions.append({"type":"transfer","amount":move,"destination account":account,"date&time":datetime.datetime.today().strftime("%m/%d/%y,%H:%M")})
    
    # defining a method for checking if the inventory won't be less than min_inventory
    def check_inventory(self,amount):
        if self.inventory - amount < self.min_inventory:
            print("Your inventory is not enough!")
            return False
        else:
            print("The operation was done successfully!")
            return True

    # defining a method for show transactions in a chosen time
    def show_trans(self,year,month,day,hour,minute):
        for i in self.transactions:
            for m in range(int(minute)-2,int(minute)+2):
                if i["date&time"]==f"{month}/{day}/{year},{hour}:{m}":
                    print(i["date&time"])



# a= Account("amir",300)
# a.deposit()
# a.withdraw()
# a.deposit()
# a.show_trans("21","09","20","00","21")

        


        
