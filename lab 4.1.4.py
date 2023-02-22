import datetime

dt1 = datetime.datetime.now()
dt2 = datetime.datetime.now() - datetime.timedelta(days = 19)
delta = dt1 - dt2
print(delta)