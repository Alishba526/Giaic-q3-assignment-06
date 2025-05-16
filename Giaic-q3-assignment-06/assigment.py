class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print( f"Student name = {self.name}, age= {self.age}")
Student=Student(name="John", age=20)
Student.display()



class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
        print("Counter object created.")

    @classmethod
    def display_count(cls):
        print(f"Total Counter objects: {cls.count}")

c1 = Counter()
c2 = Counter()
c3 = Counter()
Counter.display_count()

# practice 3
class Car:
    # public variable
    def __init__(self, brand):  
        self.brand = brand
    def Start(self):
        print(f"{self.brand} car is starting.")


my_car = Car("Mehran")
print(my_car.brand)
my_car.Start()



# practice 4
class Bank:
    bank_level = "state bank"  # Class variable

    @classmethod
    def bank_Change_name(cls, name):
        cls.bank_level = name  

b1 = Bank()
print(b1.bank_level) 

Bank.bank_Change_name("pakistan bank")

print(b1.bank_level)  

# practice 5
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Method call without creating an object
result = MathUtils.add(5, 7)
print("Sum is:", result)


# class 6
class Logger:
    def __init__(self):
        print("Logger started: Object created.")

    def __del__(self):
        print("Logger stopped: Object destroyed.")
log = Logger()

del log


# 7. Access Modifiers: Public, Private, and Protected
class Employee:

    def __init__(self,name,salary):
        self.name = name
        self._salary = salary
        self.__ssn = "321-11-7654"
    
    def show_ssn(self):
        return self.__ssn  # private variable use inside method

        
    
obj = Employee("Arif",20000)

# Public variable access outside the class
print(obj.name)  

# Protected variable access outside the class
print(obj._salary)

# print(obj.__ssn)  # not access directly so we make method

print(obj.show_ssn())




# 8. The super() Function
class Person:
    def __init__(self,name):
        self.name = name


class Teacher(Person):
    def __init__(self, name , subject ):
        super().__init__(name)
        self.subject = subject


obj = Teacher("Alishba","English")
print(obj.name)
print(obj.subject)





# 9. Abstract Classes and Methods
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Reactangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
obj = Reactangle(2,4)
print("Area:", obj.area())



# 10. Instance Methods
class Dog:
    def __init__(self , name , breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} is of {self.breed} breed."

obj = Dog("Tommy", "German Shepherd")
print(obj.bark())




# 11. Class Methods
class Book():
    total_books = 18

    @classmethod
    def increament_book_count(cls):
        cls.total_books += 1
        return cls.total_books


obj = Book()
print(Book.increament_book_count())  





# 12. Static Methods
class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        f = (c * 9/5) + 32
        return f

obj = TemperatureConverter()
print(TemperatureConverter.celsius_to_fahrenheit(20))






# Composition question 01

class Engine():
    
    def __init__(self,engine_type):
        self.engine_type = engine_type

    def start(self):
        print(f"{self.engine_type} engine started")


class Car:
    def __init__(self,engine):
        self.engine = engine
        
    def start_car(self):
        return self.engine.start()

    
obj = Engine("V8")
obj2 = Car(obj)
obj2.start_car()




# Composition question 02


class Book():
    def __init__(self,title,author,publication):
        self.title = title
        self.author = author
        self.publication = publication

    def get_info(self):
        return (f"The book {self.title} by {self.author} was published in {self.publication}")
        

class Library():
    def __init__(self,book):
        self.book = book

    def show_books(self):
        return self.book.get_info()

obj = Book("Alchemist","Paulo Coelho",1988)
obj2 = Library(obj)
print(obj2.show_books())





# 14. Aggregation

class Employee:
    def __init__(self,name,role):
        self.name = name
        self.role = role

    def display(self):
        print(f"Employee Name: {self.name}, Role: {self.role}")


class Department:
    def __init__(self,depth_name,employee):
        self.depth_name = depth_name
        self.employee = employee

    def display(self):
        print(f"Department: {self.depth_name}")
        print("Employee Info:")
        self.employee.display() # Aggregation: reference to an existing Employee object


# Pehle employee object banate hain
emp1 = Employee("Alishba","Web Developer")

# Step 2: Ab department banate hain aur employee ka reference dete hain
dept1 = Department("IT Department",emp1)

# Display karte hain
dept1.display()





# 15. Method Resolution Order (MRO) and Diamond Inheritance

" MRO (Method Resolution Order):"
"Agar ek robot ko do languages seekhni hain, ek English aur ek Urdu, to Python decide karega pehle kaunsi language seekhni hai — yehi MRO hai."


" Diamond Inheritance:"
"Agar ek vehicle ko do alag engines se power mil rahi ho, dono engines same company ke hon, to jab vehicle chalu ho, to kis engine se power li jaye — yehi diamond inheritance ka case hai."

"Now, Solve the question:"

class A:
   def show(self):
      print("Class A")


class B(A):
   def show(self):
      print("Class B")
   

class C(A):
   def show(self):
      print("Class C")


class D(B, C):
    pass

d = D()
d.show()
print(D.__mro__)





# 16. Function Decorators

"🔹 Function Decorator: Aik function jo kisi doosre function ka behavior modify ya extend karta hai bina us function ko directly change kiye."

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello World")

say_hello()





# 17. Class Decorators

"🔹 Class Decorator: Aik function jo kisi class ka behavior modify ya extend karta hai bina us class ko directly change kiye."

def add_greeting(cls):

    def greet(self):
        return "Hello from decorater"

    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self,name):
        self.name = name

person = Person("Alishba")
print(person.greet())





# 18. Property Decorators: @property, @setter, and @deleter


"🔹 @deleter: Woh decorator hota hai jo property ko delete karne ke liye method define karta hai."

class Product():

    def __init__(self,price):
        self._price = price

    
    @property
    def price(self):
        return self._price

    
    @price.setter
    def price(self,value):
        self._price = value


    @price.deleter
    def price(self):
        del self._price


p = Product(100)

print(p.price)

p.price = 200
print(p.price)

del p.price





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