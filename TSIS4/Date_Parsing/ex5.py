import datetime
def second(x, y):
    dif=x-y
    print(dif.total_seconds())
a=datetime.datetime(2023, 5, 2, 16, 25, 20)
b=datetime.datetime(2022, 6, 7, 8, 51, 20)
second(a, b)