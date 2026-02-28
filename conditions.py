#question 1
""" a=(input('enter a value: '))
if(a.isdigit() and len(a)==3):
    print(a+ " is a three digit number")
else:
    print(a+ " is not a three digit number") """

# 2
# a=input('enter a string: ')
# if(len(a)>5):
#     print(a+ " greater than 5")
# else:
#     print(a+ " not greater")


#3
#  a=(int(input('enter a number: ')))
# if(a==0):
#     print("zero")
# else:
#     print('not zero')

#4
#  a=(int(input('enter age of person: ')))
# b=(input('id is valid: '))
# if(a>=18 and id=="True"):
#     print('eligible')
# else:
#     print('not eligible')

# 5
# a=(int(input('enter a number: ')))
# if(a>=10 and a<=50):
#     print('in range')
# else:
#     print('not in range')

# 6
# a=(eval(input('enter a number: ')))
# b=(eval(input('enter a number: ')))
# op=eval(input('enter an operator: '))
# if op=='+':
#  print(a+b)
# if op=='-':
#     print(a-b)
# else:
#    print('exit')

# 7
# username=('Anushka')
# password=('1234567')
# a=((input('enter username: ')))
# b=((input('enter password: ')))
# if(a==username and b==password):
#     print('valid')
# else:
#     print('invalid')

# 8
# temp=(eval(input('enter temperature: ')))
# if(temp>=25):
#     print("temperature is hot")
# else:
#     print("temperature is cold")

# 9
# num=((input('enter number: ')))
# rev=num[::-1]
# if(num==rev):
#     print('palindrome')
# else:
#     print('not palindrome')

# 10
# num=(eval(input('enter number: ')))
# if(num > 100):
#     print('greater than 100')
# else:
#     print('not greater than 100')

# practice-1
# age=(int(input('enter age: ')))
# income=(eval(input('enter income: ')))
# credit_score=(eval(input('enter credit score: ')))
# if(age>=21):
#     if(income>=25000):
#         if(credit_score>=700):
#             print('loan approved')
#         else:
#             print('loan rejected-low credit score')
#     else:
#         print('loan rejected-low income')
# else:
#     print('loan rejected-age not eligible')    


#practice-2
#  math=(int(input('enter maths marks: ')))
# science=(int(input('enter science marks: ')))
# english=(int(input('enter english marks: ')))
# avg=(math+science+english)/3
# if(math>=40 and science>=40 and english>=40):
#     if(avg>=75):
#         print('distinction')
#     else:
#         print('pass')
# else:
#     print('fail')

income=(eval(input('enter your income: ')))
if(income>500000):
    if(income<1000000):
        print('20% tax')
    else:
        print('30% tax')
else:
    if(income>250000):
        print('5% tax')
    else:
        print('no tax')
