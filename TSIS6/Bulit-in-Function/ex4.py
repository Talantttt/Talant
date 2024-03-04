import math
import time
def root(a, second):
    time.sleep(second/1000)
    return math.sqrt(a)
print("Input:")
a = int(input())
second = int(input())
print(f"Output:\nSquare root of {a} after {second} miliseconds is {root(a, second)}")