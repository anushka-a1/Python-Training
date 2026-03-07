# global and nonlocal variables
""" a=500
def fname():
    global a
    a=1000
    b=50

    print(a+b)
    def fname2():
        # global b
        nonlocal b
        b=300
        print(b)
    fname2()
    print(b)
fname()
print(a) """


# Function to calculate the product of elements in a list
""" def fproduct(a):
    product=1
    for i in a:
        product*=i
    return product

a=[10,20,30]
print(fproduct(a)) """

# write a proggram to print initial index of character in a string
""" s=input('enter a string: ')
c=input('enter a character: ')
# def find_index(s,c):
#     return s.find(c)
def find_index(s,c):
    for i in range(len(s)):
        if s[i]==c:
            return i
    return -1 
print(find_index(s,c)) """

#unpacking
""" def unpacking(a,b,c):
    print(a,b,c)
a=[10,20,30]
unpacking(*a) """

# packing
def packing(*a):
    print(a)
packing(10,20,30)

