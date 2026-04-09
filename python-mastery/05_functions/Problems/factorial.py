'''Write a Python function to calculate the factorial of a number (a non-negative integer).
 The function accepts the number as an argument.'''
def fact(n):
    facto=1
    for i in range (1, n+1):
        facto= facto * i
    return facto
n= int(input("Enter n:"))
output = fact(n)
print("Factorial of the numbers:", output)

#using recursion function
def fact(n1):
    if n1==0 or n1==1:
        return 1
    else:
        return n1 * fact(n1-1)
n1= int(input("Enter n1:"))
output1 = fact(n1)
print("Factorial of the numbers:", output1)