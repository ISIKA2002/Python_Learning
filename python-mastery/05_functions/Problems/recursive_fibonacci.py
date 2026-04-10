def fibo(n):
    if n==0: #base case
       return 0
    elif n==1:#base case
        return 1
    else:
        return fibo(n-1) + fibo(n-2) #recursive case
    
n = int(input("Enter the number of items:"))

for i in range (n):
    print(fibo(i), end="")