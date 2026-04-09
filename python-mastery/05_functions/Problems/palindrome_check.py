#Palimdrome= 12321
n= (input("Enter the number:"))

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")