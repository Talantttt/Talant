def all_numbers(a,b):
    for i in a:
        b*=i
    print(b)
a=list((map(int, input().split())))
b=1
all_numbers(a,b)