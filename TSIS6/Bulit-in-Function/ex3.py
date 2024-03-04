def palindrome(a):
    s=input()
    a=s[::-1]
    if a==s:
        print("String is palindrome")
    else:
        print("String is not palindrome")
a=""
palindrome(a)