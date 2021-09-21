import re
import datetime
import jdatetime
import time

def calculate_time(func):
    def wrapper(*args):
        start_time=time.time()
        value=func(*args)
        print(f'time :{time.time()-start_time}s')
        return value
    return wrapper


name_1 = "Mohammad Ahmadi"
email_1 = "testmail@test.com"
phone_1 = "09123456789"
birthday_1 = "21/08/1380"
password_1 = "ItsJustTest1"

@calculate_time
def name1(name_1):
    name=re.search("\A([a-z]|[A-Z])*\s*([a-z]|[A-Z])*\s*([a-z]|[A-Z])",f"{name_1}")
    return bool(name)

@calculate_time
def phone1(phone_1):
    phone=re.search("09\d[9]\Z",f"{phone_1}")
    return bool(phone)

@calculate_time
def email1(email_1):
    email=re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",f"{email_1}")
    return bool(email)

@calculate_time
def birthday1(birthday_1):
    birthday=re.search("^(0*[1-9]|[12][0-9]|3[01])[-/.](0*[1-9]|1[012])[-/.](12|13|14)[0-9][0-9]$",f"{birthday_1}")
    return bool(birthday)

@calculate_time
def password1(password_1):
    password=re.search("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$",f"{password_1}")
    return bool(password)

def age(date):
    date=re.search("^(0*[1-9]|[12][0-9]|3[01])[-/.](0*[1-9]|1[012])[-/.](12|13|14)[0-9][0-9]$",f"{date}")
    date_list = list(map(int, date.group().split(sep=r"/")))
    jalali = jdatetime.date(day=date_list[0], month=date_list[1],year=date_list[2])
    b=jdatetime.date.today() - jalali
    print(int(b.days/365))


def resttobirth(date):
    date=re.search("^(0*[1-9]|[12][0-9]|3[01])[-/.](0*[1-9]|1[012])[-/.](12|13|14)[0-9][0-9]$",f"{date}")
    date_list = list(map(int, date.group().split(sep=r"/")))
    jalali = jdatetime.date(day=date_list[0], month=date_list[1],year=date_list[2])
    b=jdatetime.date.today() - jalali
    print((b.days%365))

resttobirth(birthday_1)

