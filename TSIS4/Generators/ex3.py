class div34:
    def __init__(self,n):
        self.a=0
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        while self.a<=self.n:
            self.a+=1
            if self.a%3==0 and self.a%4==0:
                return self.a
        raise StopIteration
myclass=div34(int(input()))
myiter=iter(myclass)
for x in myiter:
    print(x)