import datetime
# defining a method for changing the date and time format show
def date_show(year,month,day):
    # getting the details of internal argument by strptime method and save it in a datetime object 
    time=datetime.datetime.strptime(f"{year}/{month}/{day}","%Y/%m/%d")
    # use strftime to return time and date in chosen format
    print(time.strftime("%A-%B-%Y"))

# date_show("2018","6","1")