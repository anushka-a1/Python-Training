# inheritance example - inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a child or subclass) to inherit properties and behaviors (attributes and methods) from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.
""" 
class Animal: # parent class or base class
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal): # Dog class inherits from Animal class
    def sound(self):
        print("Dog barks")
class Cat(Animal): # Cat class inherits from Animal class
    # def sound(self):
    #     print("Cat meows")
    pass #pass is used when we want to create a class without any attributes or methods, it is a placeholder for future code. this is called method resolution order (MRO) in Python, when we call the sound method of Cat class, it first looks for the method in Cat class, if it is not found then it looks for the method in the parent class Animal and executes it.
d=Dog()
d.sound() #accessing the sound method of Dog class
c=Cat()
c.sound() #accessing the sound method of Cat class """


# class and object example
""" class Bank:
    def __init__(self, name, account, balance):
        self.name=name
        self.account=account
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        print("Amount deposited: ", amount)
        print("New balance: ", self.balance)
    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print("Amount withdrawn: ", amount)
            print("New balance: ", self.balance)
    def show_balance(self):
        print("Current balance: ", self.balance)
b1=Bank("Anushka", 12345, 10000) 
b2=Bank("Rohit", 54321, 20000) 
b3=Bank("Priya", 67890, 15000) 
b1.show_balance() #accessing the show_balance method of Bank class using object b1
b1.deposit(5000) #accessing the deposit method of Bank class using object b1 and depositing 5000
b1.withdraw(2000) #accessing the withdraw method of Bank class using object b1 and withdrawing 2000
b2.show_balance() 
b2.deposit(10000)
b2.withdraw(5000)
b3.show_balance()
b3.deposit(7000)
b3.withdraw(3000) """

# super method in inheritance - the super() function in Python is used to call a method from the parent class. It is commonly used in the __init__ method of a child class to initialize the attributes of the parent class.
""" class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        super().sound() #calling the sound method of parent class Animal using super() function
        print("Dog barks")
d=Dog()
d.sound() #accessing the sound method of Dog class, it will first call the sound method of Animal class and then execute the print statement in Dog class """

# example of calling parent constructor using super() function
""" class Animal:
    def __init__(self, name):
        self.name=name
        print("animal constructor called")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name) #calling the __init__ method of parent class Animal using super() function to initialize the name attribute
        print("dog constructor called")
d=Dog("Buddy") 
dog_name=d.name #accessing the name attribute of Dog class which is inherited from Animal class
print("Dog name: ", dog_name) """

# example
""" class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary) #calling the __init__ method of parent class Employee using super() function to initialize the name and salary attributes
        self.department=department

    def display(self):
        print("Name: ", self.name) #accessing the name attribute of Employee class which is inherited by Manager class
        print("Salary: ", self.salary) #accessing the salary attribute of Employee class which is inherited by Manager class
        print("Department: ", self.department) #accessing the department attribute of Manager class

m=Manager("Alice", 50000, "HR")
m.display() #accessing the display method of Manager class which will print the name, salary """

# property method = a property method in Python is a special type of method that allows you to define a method that can be accessed like an attribute. It is defined using the @property decorator and is used to calculate or retrieve a value based on the attributes of the class. When you access a property method, it automatically calls the method and returns the calculated value without needing to use parentheses like a regular method.
""" class Circle:
    def __init__(self, radius):
        self.radius=radius
    @property #decorator to define a property method
    def area(self):
        return 3.14*self.radius**2 #calculating the area of circle using the radius attribute
c=Circle(5)
print("Area of circle: ", c.area) #accessing the area property method of Circle class, it will calculate and return the area of circle based on the radius attribute
     """
# polymorphism example method overriding- polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). 
""" class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound() # method name is same but it behaves differently based on the object that is calling it, this is called polymorphism through method overriding.
 """
# polymorphism example through operator overloading
""" class Number:
    def __init__(self, value):
        self.value=value
    def __add__(self, other): #overloading the + operator to add two Number objects
        return self.value + other.value
n1=Number(10)
n2=Number(20)
print(n1 + n2) #when we use the + operator with Number objects, it calls the __add__ method and adds the values of n1 and n2, this is called polymorphism through operator overloading.
 """


# example
""" class Person:
    def __init__(self, age):
        self.age = age
    def __eq__(self, other):
        return self.age == other.age
p1 = Person(21)
p2 = Person(21)
print(p1 == p2) # when we use the == operator with Person objects, it calls the __eq__ method and compares the age attributes of p1 and p2, this is another example of polymorphism through operator overloading. """

# example
class Circle:
    def __init__(self):
        radius=eval(input('enter radius of circle: '))
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 2*3.14*self.radius
    
c=Circle()
print("Area of circle: ", c.area()) #accessing the area method of Circle class to calculate the area of circle
print("Perimeter of circle: ", c.perimeter()) #accessing the perimeter method of Circle class to calculate the perimeter of circle
