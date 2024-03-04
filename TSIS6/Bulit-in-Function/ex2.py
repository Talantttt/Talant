def count_letter(a):
    c_low=0
    c_upp=0
    for i in a:
        if i.islower():
            c_low+=1
        elif i.isupper():
            c_upp+=1
    print("Number upper case letters:", c_upp)
    print("Number lower case letters:", c_low)

a=input()
count_letter(a)