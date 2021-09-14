from datetime import datetime, timedelta

start_time=datetime(2018,2,19,14)
duration= timedelta(hours=8)
alarms=[]

for i in range(1,11):
    alarms.append(start_time + i*duration)

remained=0
for i in range(10):
    if alarms[i]>start_time:
        remained += 1
print(remained)

for i in range(10):
    if alarms[i]>start_time:
        print(alarms[i]-start_time)
        exit()



