#Fibonacci series
# Fibonacci series: each number = sum of previous two numbers. [0+1=1, 1+1=2, 1+2=3,...]
num=int(input("Enter the number of items:"))
a=0
b=1
for i in range(num):
    print(a, end="")
    c = a+b
    a = b
    b = c   