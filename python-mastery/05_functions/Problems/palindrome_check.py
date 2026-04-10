#Palimdrome= 12321
n = (input("Enter the number:"))

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#without string or using math
num=int(input("Enter the number:"))

temp=num
rev=0

while num>0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")    
