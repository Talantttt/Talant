import datetime
x=datetime.datetime.now()
print("Yesterday:", x-datetime.timedelta(days=1))
print("Tomorrow:",x+datetime.timedelta(days=1))