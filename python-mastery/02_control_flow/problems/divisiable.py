#Take a posetive ingeter input and tell it is divisible by 5 or 3 not divisible by 15
num= int(input("Enter a number:"))
#Checking if divisible by 15 or not (use if else)
if num % 15 ==0:
    print("Number is divisible by 15")
else:
    #Checking divisible by 3 or 5
    if num % 3==0 or num % 5 ==0:
        print("Number is not divisible by 15 but divisible by 3 and 5")  
    else:
        print("Number is neither divisible by 3 and 5")