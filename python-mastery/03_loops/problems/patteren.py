#Print for n=n_number 
#Example
#*****
'''n= int(input("Enter n:"))
for i in range(n):
    print("*" * 5)'''

#Print for n=n_number(let it be 1,2,3..)
#Example
#*
#**
#***
#****
'''n= int(input("Enter n:"))
for i in range(1, n+1):
    print("*" * i)'''

#Print for n=n_number(let it be 1,2,3..)
#Example
#****
#***
#**
#*
'''n= int(input("Enter n:"))
for i in range(n, 0, -1):
    print("*" * i)'''

#Print for n=n_number
#Example
#1234
#1234
#1234
#1234
'''r = int(input("Enter r:"))
for i in range(r):
    for c in range(1, r+1):
      print(c, end="")
    print()'''

#Print for n=n_number(let it be 1,2,3..)
#Example
#1
#12
#123
#1234
'''r = int(input("Enter r:"))
for i in range(1, r+1):
    for c in range(1, i+1):
         print(c, end="")
    print()  ''' 

#Print for n=n_number(let it be 1,2,3..)
#Example
#1234
#123
#12
#1
'''r= int(input("Enter r:"))
for i in range(r, 0, -1):
    for c in range(1, i + 1):
        print(c, end="")
    print()'''

#Print for n=n_number(let it be 1,2,3..)
#Example
#A
#AB
#ABC
#ABCD
'''r = int(input("Enter r:"))
for i in range(1, r+1):
    for j in range(i):
        print(chr(65 + j), end="")
    print() ''' 

#Print for n=n_number(let it be 1,2,3..)
#Example
#ABCD
#ABC
#AB
#A
'''r = int(input("Enter r:"))
for i in range(r, 0, -1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()'''    

#Print for n=n_number 
#Example
#   1  
#  123
# 12345
#1234567
'''r = int(input("Enter r:"))
for i in range(1, r+1):
    print(" " * (r-i), end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()'''    

#print for n=n_number(let it be 1,2,3..)
#Example
#1234567
# 12345
# 123
# 1
'''r= int(input("Enter r:"))
for i in range(r):
    for j in range(i):
        print(" ", end="")
    for q in range(1, 2*(r-i)):
        print(q, end="")
    print() '''