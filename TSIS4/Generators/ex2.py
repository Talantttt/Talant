class even:
    def __init__(self,n):
        self.n=n
        self.a=-2
    def __iter__(self):
        return self
    def __next__(self):
        self.a+=2
        if self.a<=self.n:
            return self.a
        elif self.a>self.n:
            raise StopIteration
myclass=even(int(input())) 
myiter=iter(myclass)
results=[str(x) for x in myiter]
print(", ".join(results))