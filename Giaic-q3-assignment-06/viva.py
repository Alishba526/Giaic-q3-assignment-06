# viva practice
# # # class Alishba:
# # #     def __init__(self ,name,salay):
# # #         self.name = name
# # #         self.salay = salay

# # #     def display_info(self):
# # #             print(f"Employee name is {self.name} and salary is {self.salay}")

# # # # object creation
# # # emp1 = Alishba("alishba","$50000")
# # # emp1.display_info()


# # # class Car:
# # #     def __init__(self,name,model):
# # #         self.name = name
# # #         self.model = model

# # #     def display_info(self):
# # #         print(f"Car name is {self.name} and model is {self.model}")

# # # # object creation
# # # car1 = Car("BMW","X5")
# # # car1.display_info()





# # # 

# # # class vichecle:
# # #     def __init__(self, name, model):
# # #         self.name = name
# # #         self.model = model

# # #     def display_info(self): 
# # #         print(f"Vichecle name is {self.name} and model is {self.model}")

# # #         class Car(vichecle):
# # #             def __init__(self, name, model, color):
# # #                 super().__init__(name, model)
# # #                 self.color = color

# # #             def display_info(self):
# # #                 print(f"Car name is {self.name} and model is {self.model} and color is {self.color}")
# # #                 self.department=vichecle
# # #                 m1= Car("BMW","X5","red")
# # #                 m1.display_info()
# # #                 m1.department








# # # # class Lion:
# # # #     def __init__(self, name, age):
# # # #         self.name = name
# # # #         self.age = age

# # # #     def display_info(self):
# # # #         print(f"Lion name is {self.name} and age is {self.age}")
# # # # m1= Lion("Simba", 7)
# # # # m1.display_info()

















# # # # class Lion:
# # # #     def __init__(self, name, age):
# # # #         self.name = name
# # # #         self.age = age

# # # #     def display_alish(self):
# # # #         print(f"Lion name is {self.name} and age {self.age}")

# # # # m1 = Lion("sameer", 7)
# # # # m1.display_alish()
            


# # # # class Lion:
# # # #     def __init__(self, name, age):
# # # #         self.name = name
# # # #         self.age = age
# # # #         print(f"name is{name} age is {age}")
# # # # m1=Lion("ahugb",6)
  

# # # # 🔹 3. Class aur Object
# # # # class Person:
# # # #     def __init__(self, name):
# # # #         self.name = name

# # # #     def greet(self):
# # # #         print(f"Hello, my name is {self.name}")

# # # # p1 = Person("Ali")
# # # # p1.greet()
# # # # Roman Urdu: class aik design hai, aur object us design ka actual piece hota hai.

# # # # # 🔹 4. Constructor (__init__ method)
# # # # class Car:
# # # #     def __init__(self, brand):
# # # #         self.brand = brand
# # # #         print(f"Car brand is {self.brand}")

# # # # my_car = Car("Toyota")
# # # # __init__ constructor hota hai, jab bhi object banta hai to yeh method automatic chalta hai.

# # # # 🔹 5. Inheritance (Warasat)


# # # class Animal:
# # #     def eat(self):
# # #         print("Animal is eating")

# # # class Dog(Animal):
# # #     def bark(self):
# # #         print("Dog is barking")

# # # d = Dog()
# # # # d.eat()
# # # # d.bark()
# # # # # Roman Urdu: Dog class ne Animal se functions inherit kiye hain. eat() parent ka function hai.

# # # # # 🔹 6. Encapsulation









# # # # encapsulation
# # # class private_variable:
# # #     def __init__(self,name):
# # #         self.__name=name

# # #     def get_name(self):
# # #         return self.__name

# # # m1 = private_variable("Ali")
# # # print(m1.get_name())  

# # # # abtraction
# # # from abc import ABC, abstractmethod
# # # class vehicle(ABC):
# # #     @abstractmethod
# # #     def drive(self):
# # #         pass

# # #     @abstractmethod
# # #     def stop(self):
# # #         pass

# # #     # real 

# # #     class realwork():
# # #         def drive(self):
# # #             print("Vehicle is driving")

# # #         def stop(self):
# # #             print("Vehicle is stopping")

# # #     m2=realwork()
# # #     m2.drive()
# # #     m2.stop()
# # from abc import ABC, abstractmethod
# # class vehicle(ABC):
# #     @abstractmethod
# #     def runaway(self):
# #         pass

# #     @abstractmethod
# #     def stop(self):
# #         pass

# # # real working

# # class childclass(vehicle):
# #     def runaway(self):
# #         print("Vehicle is running away")
    
# #     def stop(self):
# #         print("Vehicle is stopping")

# # # Create an instance of childclass and call its methods
# # child = childclass()
# # child.runaway()
# # child.stop()
   

























# # from abc import ABC, abstractmethod

# # class Car(ABC):
# #     @abstractmethod
# #     def engine_start(self):
# #         pass

# #     @abstractmethod
# #     def engine_stop(self):
# #         pass

# # # real work ab 

# # class Break(Car):
# #     def engine_start(self):
# #         print("Break is applied")

# #     def engine_stop(self):
# #         print("Break is released")

# # # Example usage:
# # b = Break()
# # b.engine_start()
# # b.engine_stop() 







# from abc import ABC,abstractmethod

# class House(ABC):
#     @abstractmethod
#     def semit(self):
#         pass


#     @abstractmethod
#     def matti(self):
#         pass


#     # realwork
# class Houses1(House):
#   def semit(self):
#       print(f"semit se house bane ga")


#   def matti(self):
#         print(f"house bana hoga ")

# p=Houses1()
# p.semit()
# p.matti()






# class Encapsoution():
#     def __init__(self,name ,model):
#         self.__name = name
#         self.__model=model

# def Name(self):
#     return self.__name.__model
# p1=Encapsoution("Ali","BMW")
# print(Name(p1))   












# # # # # encapsulation
# # # # class private_variable:
# # # #     def __init__(self,name):
# # # #         self.__name=name

# # # #     def get_name(self):
# # # #         return self.__name

# # # # m1 = private_variable("Ali")
# # # # print(m1.get_name())


# # single inheritance

# class Prent():
#     def greet(self):
#         print("Hello prents")

# class Child(Prent):
#     def greet1(self):
#         print("Hello Child")

# n = Child()
# n.greet()
# n.greet1()





# mul inheritance

# class Prent1():
#     def greet(self):
#         print("Hello prents1")
# class Prent2():
#     def hello(self):
#         print("Hello prents2")
# class Child(Prent1,Prent2):
#     def greet1(self):
#         print("Hello Child3")

# n = Child()
# n.greet()
# n.hello()    
# n.greet1()



class Parent():
    def greet(self):
        print("Hello brave")

class Child(Parent):

    def Child1(self):
     super().greet()
    print("hello ggggggg")
    def greet1(self):
        print("Hello Child")
f=Child()
f.greet1()
f.Child1()





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
