# pattern 1 basic pattern
""" for i in range(1,4):
    for j in range(1,4):
        print("*",end="")
    print() """

# pattern 2 taking number of rows as input
""" i=int(input('enter a number: '))
for j in range(1,i+1):
    for k in range(1,i+1):
        print("*",end=" ")
    print() """

# pattern 3 taking rows and columns as input
""" i=int(input('enter number of rows: '))
j=int(input('enter number of columns: '))
for i in range(1,i+1):
    for j in range(1,j+1):
        print("*",end=" ")
    print() """

# pattern 4 primary diagonal pattern
""" for i in range(1,5):
    for j in range(1,i+1):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()     """

# pattern 5 upper and lower triangle with primary diagonal
""" for i in range(1,5):
    for j in range(1,5):
        if i==j:
            print("*",end=" ")
        elif i<j:
            print("@",end=" ")
        elif i>j:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()  """

# pattern 6 secondary diagonal
""" n=int(input('enter the size of the matrix: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()  """


# pattern 7 upper and lower triangle with secondary diagonal
""" n=int(input('enter the size of the matrix: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print("#",end=" ")
        elif i+j<n+1:
            print("*",end=" ")
        elif i+j>n+1:
            print("@",end=" ")
        else:
            print(" ",end=" ")
    print() """

# pattern 8 primary and secondary diagonal
for i in range(1,4):
    for j in range(1,4):
        if i+j==4:
            print("#",end=" ")
        elif i==1 and j==1:
            print("*",end=" ")
        elif i==3 and j==3:
            print("@",end=" ")
        else:
            print(" ",end=" ")
    print()

