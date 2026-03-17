#Write a program to swap the two elements in the list.
n= int(input("Input length of the list:"))
list=[]
for i in range(n):
    num=input()
    list.append(num)
print("Before swaping the list is:", list)
indx1=int(input("Enter the index1:"))
indx2=int(input("Enter the index2:"))

temp=list[indx1]
list[indx1]= list[indx2]
list[indx2]= temp
print("After swap the list is:", list)