import redis
import logging
from datetime import datetime

DB = redis.Redis(encoding="utf-8", decode_responses=True)
logging.basicConfig(filename='ticket.log', level=logging.DEBUG)
# defining a class for creating evet
class System:
    password1="1234abcd"
    admin=False
    event_num=0
    discounts={
        "teacher":[457,755,443,343],
        "student":[343,453,545,234],
        "employee":[232,546,987,984],
        "artist":[432,165,189,100]
    }
    def __init__(self,password):
        # checking the password
        if password!=System.password1:
            logging.error(f'{datetime.now()}:Wrong password!')
            del self
        else:
            self.admin=True
            logging.info(f'{datetime.now()}:Admin logged in!')
    # defining a method for adding a new event
    @staticmethod
    def add_event(date,location,capacity,left,cost):
        DB.hset(f'event:{System.event_num}',mapping={
            "event_number": System.event_num,
            "date": date,
            "location": location,
            "capacity": int(capacity),
            "cost": int(cost),
            "left": int(left)
        })
        System.event_num += 1
        logging.info(f'{datetime.now()}:event number {System.event_num} created!')
# defining a class for who want to buy a ticket
class User:
    def __init__(self,name,discount_code,person=None):
        self.name=name
        self.person=person
        self.discount_code=discount_code
    # defining a method for displaying events
    @staticmethod
    def event_show():
        i = 1
        for i in range(1,System.event_num+1):
            print('event number:', DB.hget(f'event:{i}', 'event_number'))
            print('date:', DB.hget(f'event:{i}', 'date'))
            print('location:', DB.hget(f'event:{i}', 'location'))
            print('capacity:', DB.hget(f'event:{i}', 'capacity'))
            print('cost:', DB.hget(f'event:{i}', 'cost'))
            print('tickets remaining:', DB.hget(f'event:{i}', 'left'))

    # defining a method for buying ticket
    def buy_ticket(self,event_number,count):
        cost = int(DB.hget(f'event:{event_number}', 'cost'))
        left = int(DB.hget(f'event:{event_number}', 'left'))
        
        # checking if discount code is right
        if self.discount_code in System.discounts[self.person]:
            cost = cost * 0.8 * count
        else:
            cost = cost * count
        # checking if remained tickets are enough
        if left < count:
            print(f'{left} tickets are remaining')
            logging.warning(f'{datetime.now()}:unsuccessful buy for event number {event_number}')
        else:
            print("ticket has bought!")
            logging.info(f'{datetime.now()}: ticket for event number {event_number} with {cost} payment has bought!')
            left -= count
            # set again remained tickets number because of decreasing
            DB.hset(f'event:{event_number}',mapping={"left":left})

            
    

# defining a function for running app in som environment
def program():
    exit=0
    while exit==0:
        print("\nWelcome to my awful ticket buying system:\n\n")
        print("tell me right now, who are you?")
        print("1-admin")
        print("2-very usual person")
        print("3-i wanna exit from this prison")
        choice=input()
        if choice=='1':
            print("hard choice,tell night secret:")
            password=input("password:")
            admin=System(password)
            print("now for creating a new event you should tell some information:")
            date=input("date:")
            location=input("location:")
            cost=input("cost:")
            capacity=input("capacity:")
            left=capacity
            admin.add_event(date,location,capacity,left,cost)

        if choice=='2':
            print("ok, now tell me if you are in one of this groups:")
            print("1-student")
            print("2-teacher")
            print("3-employee")
            print("4-artist")
            i=input("group:")
            if i=='1':
                person="student"
            elif i=='2':
                person="teacher"
            elif i=='3':
                person="employee"
            elif i=='4':
                person="artist"
            else:
                person=None

            name=input("Please enter your name:")
            print("do you have any discount code:")
            print("1-Yes")
            print("2-No")
            j=input()
            if j=='1':
                discount_code=int(input("Please enter your code:"))
            else:
                discount_code=0

            user=User(name,discount_code,person)
            
            print("please enter your favorite event:")
            user.event_show()
            event_number=input("event_number:")
            count=int(input("please enter the count of ticket:"))
            user.buy_ticket(event_number,count)

        if choice=='3':
            exit=1
            

# program()
             






        


        

    




        
