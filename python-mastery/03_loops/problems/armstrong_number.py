#Armstrong number [example: 153= 1**3 + 5**3 + 3**3]
num= int(input("Enter the number:")) 
sum=0
order=len(str(num))
c_num=num
while(num > 0):
    digit = num % 10 #153%10=3, 15%10=5, 1%10=1
    sum= sum+ digit**order #untill num=0
    num = num//10

if sum==c_num:
    print(c_num, "is an armstrong number")
else:
    print(c_num, "is not an armstrong number")    