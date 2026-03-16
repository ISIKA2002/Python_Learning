#Fibonacci series
num=int(input("Enter the number of items:"))
a=0
b=1
for i in range(num):
    print(a, end="")
    c = a+b
    a = b
    b = c   