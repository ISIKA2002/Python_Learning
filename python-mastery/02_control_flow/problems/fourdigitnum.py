#Take a posetive integer input and tell if it is four digit number or not
num= int(input("Enter a number:"))
if num >= 1000 and num <= 9999:
   print(num, "number is a fore digit posetive number")
else:
   print(num, "number is not a four digit posetive number")