# factorial of number without recursion
""" n=(eval(input('enter a number: ')))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)
 """
# factorial of number with recursion
""" import sys
sys.setrecursionlimit(10**6)
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=eval(input('enter a number: '))
print(fact(n)) """

# write a program to create a funnction which adds minimum two numbers and maximum five numbers taking uswer input
""" def add(*args):
    if len(args)<2 or len(args)>5:
        print("please enter between 2 and 5 numbers")
        return None
    else:
        return sum(args)
numbers=[]
n=int(input("how many numbers do you want to add? "))
for i in range(n):
    num=eval(input("enter a number: "))
    numbers.append(num)
result=add(*numbers)
if result is not None:
    print("the sum is: ", result)    """   

    

# write a program to find out the sum of individual digits of a number using recursion
""" def sum(n):
    if n==0:
        return 0
    else:
        return n%10 + sum(n//10)
n=eval(input('enter a number: '))
print(sum(n)) """


class Student:
    name = "Anushka"
    age = 21

s1 = Student()

print(s1.name)
print(s1.age)
