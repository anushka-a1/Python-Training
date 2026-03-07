# positional arguments
""" def form(name, mail, ph, age):
    print("Name: ", name)
    print("Email: ", mail)
    print("Phone: ", ph)
    print("Age: ", age)
form("Anushka", "anushka@example.com", "1234567890", 22) """

# default arguments
""" def form(name, mail, ph, age):
    print("Name: ", name)
    print("Email: ", mail)
    print("Phone: ", ph)
    print("Age: ", age)
form("Anushka", "anushka@example.com", "1234567890")  #age value is taken as defsult value """

""" def form(name, mail, ph, age=20, alt_ph=None): #age and alt_ph are default arguments because they are done at function declaration
    print("Name: ", name)
    print("Email: ", mail)
    print("Phone: ", ph)
    print("Age: ", age) 
    print("Alternate Phone: ", alt_ph)
form("Anushka", "anushka@example.com", "1234567890", alt_ph="0987654321")  """

# keyword arguments
""" def form(name, mail, ph, age=20, alt_ph=None):
    print("Name: ", name)
    print("Email: ", mail)
    print("Phone: ", ph)
    print("Age: ", age) 
    print("Alternate Phone: ", alt_ph)
form("Anushka", "anushka@example.com", "1234567890", alt_ph="0987654321")  #here it is done at function calling so it is keyword argument """

# variable length arguments
""" def form(**a):
    print('a:', a)
    print('Length of a:', len(a))
form(e="Anushka", b="anushka@example.com", c=12345, d=9087) """ #collects keyword arguments in a dictionary

""" def form(*a):
    print('a:', a)
    print('Length of a:', len(a))
form("Anushka", "anushka@example.com", 12345, 9087) """ #collects positional arguments in a tuple 

# all arguments example taking user input
def form(name, mail, ph, age, *marks, **details):
    print("Name: ", name)
    print("Email: ", mail)
    print("Phone: ", ph)
    print("Age: ", age) 
    print("Marks: ", marks)
    print("Details: ", details)
name=input('enter name: ')
mail=input('enter email: ')
ph=input('enter phone number: ')
age=int(input('enter age: '))
marks=[]
for i in range(5):
    mark=int(input('enter mark: '))
    marks.append(mark)
details={}
details['address']=input('enter address: ')
details['city']=input('enter city: ')



form(name, mail, ph, age, *marks, **details)

