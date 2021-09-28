import datetime

class Card:
    def __init__(self,credit):
        self.credit=credit
    
    def charge(self,add):
        self.credit += add
    
    def use(self):
        if self.checkcredit(100):
            self.credit -= 100
            return True
        else:
            print("credit not efficient!")
            return False
    
    def checkcredit(self,amount):
        if self.credit-amount>=0:
            return True
        else:
            return False   

class Creditcard(Card):
    pass

class Timecreditcard(Card):
    def __init__(self, credit):
        super().__init__(credit)
        self.expiration=datetime.datetime.now()
        self.renew()

    def checkexp(self,today):
        if self.expiration > today:
            return True
        else:
            return False

    def renew(self):
        self.expiration += datetime.timedelta(days=30)
    
    def use(self):
        if self.checkexp(datetime.datetime.today()):
         return super().use()
        else:
            print("card has expired!")
            return False

class Singlecard(Card):
    def __init__(self):
        super().__init__(100)



