#Write a function that print sum of 2 num
def sum(x,y):
    ans=x+y
    return ans    
print(sum(4,6))

#write a function that print Hello world
#Definbe a function
def printhello():
    #bosy of the function
    print("Hello world!")
#Call the function
printhello()

#Types of arguments
#1.Default argument
def add(n1=0, n2=0):
    sum=n1+n2
    return sum
print("Default argument(Sum):", add())

#Position argument
def add(m1, m2):
    print("m1:", m1)
    print("m2:", m2)
    sum=m1+m2
    return sum
print("Position argument(Sum):", add(2,3))

#Keyword argument
def add(p1,p2):
    sum= p1+p2
    return sum
print("Keyword argument(Sum):", add(p1=2, p2=3))

#Arbitary argument
#For *args
def addallNumbers(*args):
    sum=0
    for i in args:
        sum= sum+i
    return sum
#output= addallNumbers(1,2,3,4)
print("Submition:", addallNumbers(1,2,3,4))

#for **kwargs
def studentinfo(**kwargs):
    for x,y in kwargs.items():
        print(x, "is", y)
studentinfo(name="John", age=40, city="BBSR")
studentinfo(name="Rok", age=30, city="BNG")