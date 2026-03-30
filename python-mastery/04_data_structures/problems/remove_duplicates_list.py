#Remove duplicate list
list= input("Enter numbs:").split()
uni=[]
for i in list:
    if i not in uni:
        uni.append(i)
print("After remove the elements:", uni)
