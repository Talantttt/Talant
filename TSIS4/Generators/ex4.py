class square:
    def __init__(self, a, b):
        self.a=a
        self.b=b
        self.current=self.a-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<self.b:
            self.current+=1
            return self.current**2
        else:
            raise StopIteration
a=int(input())
b=int(input())
myclass=square(a, b)
myiter=iter(myclass)
for x in myiter:
    print(x)