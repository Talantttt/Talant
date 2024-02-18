class Numbers:
    def __init__(self, N):
        self.N=N
        self.a=0
    def __iter__(self):
        return self
    def __next__(self):
        self.a+=1
        if self.a!=1 and self.a<=self.N:
            x=self.a            
            return x**2
        elif self.a==1:
            x=self.a
            return x
        else:   
            raise StopIteration
myclass=Numbers(int(input()))
myiter=iter(myclass)
for x in myiter:
    print(x)