class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        print(f"{self.amount} {self.currency}s" if self.amount != 1 else f"{self.amount} {self.currency}")
        return f"{self.amount} {self.currency}s" if self.amount != 1 else f"{self.amount} {self.currency}"
    
    def __int__(self):
        print(self.amount)
        return self.amount

    def __repr__(self):
        return(self.__str__())
    
    def __add__(self, other):
        if isinstance(other, int):
            output = self.amount + other
            print(output)
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add Currency type <{self.currency}> and <{other.currency}>")
            print(self.amount + other.amount)
            
    def __iadd__(self, other):
        if isinstance(other, int):
        # Increment the amount by an integer
            self.amount += other
        elif isinstance(other, Currency):
        # Check if both currency types match
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        # Increment the amount by the other Currency's amount
            self.amount += other.amount
        else:
        # Return NotImplemented if the type is unsupported
            return NotImplemented
        return self  # Return self to enable in-place addition
    
    def info(self):
    #  print(({self.currency},{self.amount}))
     return f'{self.currency},{self.amount}'
    
    
    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

str(c1)
int(c1)
repr(c1)
c1 + 5
int(c1)
c1+c2
c1+=5
c1+=c2
print(c1)
# c1+c3


