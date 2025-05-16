# viva practice



# 19. callable() and __call__()



class Multiplier:
    def __init__(self,factor):
        self.factor = factor

    def __call__(self,value):
        return value * self.factor
    
multiply = Multiplier(3) 

result = multiply(2)

print(result)
print(callable(multiply))





# 20. Creating a Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18")
    else:
        print("Age is valid.")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e}")




class Countdown:
    def __init__(self, start):
        self.start = start  
        self.current = start  

    def __iter__(self):
        return self  
    
    def __next__(self):
        if self.current > 0:
            self.current -= 1  
            return self.current  
        else:
            raise StopIteration  

countdown = Countdown(10)

for num  in countdown:
    print(num)