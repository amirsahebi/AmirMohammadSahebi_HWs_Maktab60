class Account:
    # defining a amount for minimum of inventory
    min_inventory=5
    def __init__(self,name,inventory):
        self.name=name
        self.inventory=int(inventory)

    # defining a method for depositing from account
    def deposit(self):
        add=int(input("Please enter the amount:"))
        self.inventory += add
    
    # defining a method for withdraw from account
    def withdraw(self):
        reduce=int(input("Please enter the amount:"))
        if self.check_inventory(reduce):
            self.inventory -= reduce

    # defining a method for transfer to another account
    def transfer(self,account):
        move=int(input("Please enter the amount:"))
        if self.check_inventory(move):
            self.inventory -= move
            account.inventory += move
    
    # defining a method for checking if the inventory won't be less than min_inventory
    def check_inventory(self,amount):
        if self.inventory - amount < self.min_inventory:
            print("Your inventory is not enough!")
            return False
        else:
            print("The operation was done successfully!")
            return True
        


        
