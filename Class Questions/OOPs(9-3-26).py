""" # Class and Object in Python
class College: #creating a class named College
    c_name="JECRC" #c_name and loc are attributes of class College
    loc="Jaipur"
s1=College() #s1 is an object of class College
print(s1.c_name) #accessing class attribute using object
print(s1.loc)
s1.name="Anushka" #name is an attribute of object s1
print(s1.name) #accessing object attribute """

# class and object with default attributes
""" class Cars:
    car_name="Audi" #attributes of class cars
    car_color="Red" 
    car_price=5000000
c1=Cars() #c1 and c2 are objects of class Cars
c2=Cars()
c1.name="BMW" #name, color and price are attributes of object c1 and c2
c1.color="Black"
c1.price=6000000
c2.name="Mercedes"
c2.color="White"
c2.price=7000000
print(c1.car_name, c1.car_color, c1.car_price) #accessing class attributes using objects
print(c2.car_name, c2.car_color, c2.car_price)
print(c1.name, c1.color, c1.price) #accessing object attributes using objects
print(c2.name, c2.color, c2.price) """

# Constructor in Python
""" class College:
    c_name="JECRC"
    loc="Jaipur"
    def __init__(self, name, id, age): #constructor is a special method which is called when an object is created and it is used to initialize the attributes of the object
        self.name=name #self is a reference to the current object and it is used to access the attributes and methods of the class
        self.id=id
        self.age=age #name, id and age are attributes of object which are initialized using constructor
s1=College("Anushka", 12345, 21) #creating an object s1 of class College and passing values to the constructor
print(s1.c_name) #accessing class attributes using object s1
print(s1.loc)
print(s1.name) #accessing object attributes using object s1
print(s1.id)
print(s1.age) """

# exammple of constructor
""" class Cars:
    car_name="Audi"
    car_color="Red"
    car_price=5000000
    car_type="SUV"
    car_brand="Audi"
    def __init__(self, name, color, price, type, brand):
        self.name=name
        self.color=color
        self.price=price
        self.type=type
        self.brand=brand
    def display(self): #method to display the attributes of the object
        print("Car Name: ", self.name)
        print("Car Color: ", self.color)
        print("Car Price: ", self.price)
        print("Car Type: ", self.type)
        print("Car Brand: ", self.brand)
c1=Cars("BMW", "Black", 6000000, "Sedan", "BMW")
c2=Cars("Mercedes", "White", 7000000, "SUV", "Mercedes")
c3=Cars("skoda", "Grey", 3000000, "Hatchback", "Skoda")
print(c1.car_name, c1.car_color, c1.car_price, c1.car_type, c1.car_brand) #accessing class attributes using object c1

 print(c1.name, c1.color, c1.price, c1.type, c1.brand) #accessing object attributes using object c1
print(c2.name, c2.color, c2.price, c2.type, c2.brand) 
print(c3.name, c3.color, c3.price, c3.type, c3.brand) 
c1.display() #accessing method of class Cars using object c1
c2.display()
c3.display() """

# object methods
""" class Cars:
    car_name="Audi"
    car_color="Red"
    car_price=5000000
    car_type="SUV"
    car_brand="Audi"
    def __init__(self, name, color, price, type, brand):
        self.name=name
        self.color=color
        self.price=price
        self.type=type
        self.brand=brand
    def display(self): #display is an object method which is used to display the attributes of the object. It is defined inside the class and it can be accessed using the object of the class.
        print("Car Name: ", self.name)
        #updating the color in display method
        self.color="Blue" #modifying object attribute color using self in display method
        print("Car Color: ", self.color)
        print("Car Price: ", self.price)
        print("Car Type: ", self.type)
        print("Car Brand: ", self.brand)
    def update_price(self, new_price): #update_price is an object method which is used to update the price of the car. It takes new_price as a parameter and updates the price attribute of the object.
        self.price=new_price
        print("Updated Price: ", self.price)
c1=Cars("BMW", "Black", 6000000, "Sedan", "BMW")
c2=Cars("Mercedes", "White", 7000000, "SUV", "Mercedes")
c3=Cars("skoda", "Grey", 3000000, "Hatchback", "Skoda")
c1.update_price(6500000) #updating the price of car c1
c2.update_price(7500000) #updating the price of car c2
c3.update_price(3500000) #updating the price of car c3
c1.display() #accessing method of class Cars using object c1
c2.display() 
c3.display() """

# Class methods
""" class Cars:
    car_name="Audi"
    car_color="Red"
    car_price=5000000
    car_type="SUV"
    car_brand="Audi"
    def __init__(self, name, color, price, type, brand):
        self.name=name
        self.color=color
        self.price=price
        self.type=type
        self.brand=brand
    def display(self):
        print("Car Name:", self.name)
        print("Car Color:", self.color)
        print("Car Price:", self.price)
        print("Car Type:", self.type)
        print("Car Brand:", self.brand)
    @classmethod  #decorator which is used to define a class method which is a method that is bound to the class and not the object of the class. 
    def show_default_car(cls): #cls is a reference to the class and it is used to access the attributes and methods of the class. It is used as a parameter in class method.
        print("Default Car Name:", cls.car_name)
        print("Default Car Color:", cls.car_color)
        print("Default Car Price:", cls.car_price)
        print("Default Car Type:", cls.car_type)
        print("Default Car Brand:", cls.car_brand)
        cls.car_name="Maruti" #modifying class attributes using class method
        print("Modified Default Car Name:", cls.car_name) #accessing modified class attribute using class method
c1=Cars("BMW", "Black", 6000000, "Sedan", "BMW")
c2=Cars("Mercedes", "White", 7000000, "SUV", "Mercedes")
c3=Cars("Skoda", "Grey", 3000000, "Hatchback", "Skoda")
Cars.show_default_car()
c1.display()
c2.display()
c3.display()  """

# Static methods
""" class Cars:
    car_name="Audi"
    car_color="Red"
    car_price=5000000
    car_type="SUV"
    car_brand="Audi"
    def __init__(self, name, color, price, type, brand):
        self.name=name
        self.color=color
        self.price=price
        self.type=type
        self.brand=brand
    def display(self):
        print("Car Name:", self.name)
        print("Car Color:", self.color)
        print("Car Price:", self.price)
        print("Car Type:", self.type)
        print("Car Brand:", self.brand)
    #static method is used like a normal function which is defined inside the class and it can be accessed using the class name or the object of the class. It does not take self or cls as a parameter and it cannot access the attributes and methods of the class.
    @staticmethod #decorator which is used to define a static method which is a method that is bound to the class and not the object of the class. It does not take cls or self as a parameter and it cannot access the attributes and methods of the class.
    def road_tax(price): #static method 
        tax = price * 0.10
        print("Road Tax:", tax)
    @staticmethod
    def show_message(): #static method which is used to display a message. It does not take any parameter and it cannot access the attributes and methods of the class.
        print("Welcome to the world of Cars!")
c1=Cars("BMW", "Black", 6000000, "Sedan", "BMW")
c2=Cars("Mercedes", "White", 7000000, "SUV", "Mercedes")
c3=Cars("Skoda", "Grey", 3000000, "Hatchback", "Skoda")
Cars.show_message() #accessing static method using class name
Cars.road_tax(6000000) #accessing static method using class name
c1.display()
c2.display()
c3.display() """

# abstraction in Python

class Car:
    def __init__(self):
        self.acc=False
        self.clutch=False
        self.brk=False
    def start(self):
        self.acc=True
        self.clutch=True
        self.brk=False
        print("Car started") #abstraction is a process of hiding the implementation details and showing only the functionality to the user. In this example, we have created a class Car which has three attributes acc, clutch and brk which are initialized to False in the constructor. We have also created a method start which sets the acc and clutch to True and brk to False and prints "Car started". The user does not need to know how the car is started, they just need to know that when they call the start method, the car will start. This is an example of abstraction in Python.
c1=Car()
c1.start()

# encapsulation in Python
class Car:
    def __init__(self):
        self.__acc=False #private attribute which is not accessible outside the class
        self.__clutch=False
        self.__brk=False
    def start(self):
        self.__acc=True
        self.__clutch=True
        self.__brk=False
        print("Car started") #encapsulation is a process of wrapping the data and the methods that operate on the data into a single unit. In this example, we have created a class Car which has three private attributes __acc, __clutch and __brk which are initialized to False in the constructor. We have also created a method start which sets the __acc and __clutch to True and __brk to False and prints "Car started". The user cannot access the private attributes directly, they can only access them through the public method start. This is an example of encapsulation in Python.    
c1=Car()
c1.start()
