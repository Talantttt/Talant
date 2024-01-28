#Unpacking a Tuple 
fruits=("apple", "banana", "cherry")

(green, yellow, red)=fruits
print(green)
print(yellow)
print(red)
print("\n")

#Using Asterisk
fruits=("apple", "banana", "cherry", "strawberry", "rasberry")

(green, yellow, *red)=fruits
print(green)
print(yellow)
print(red)
print("\n")

#Add a list of values the "tropic" variable:
fruits=("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red)=fruits
print(green)
print(tropic)
print(red)
