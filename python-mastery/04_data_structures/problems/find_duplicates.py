#Find duplicate
'''mylist=[1,2,3,4,2,4,1,5,6]
dup=[]
uni=[]
for i in mylist:
    if i not in uni:
       uni.append(i)
    else:
      dup.append(i)
print(uni)
print(dup)         
'''
nums = input("Enter numbers: ").split()

seen = []
duplicates = []

for i in nums:
    if i in seen:
        if i not in duplicates:
            duplicates.append(i)
    else:
        seen.append(i)

print("Duplicate elements:", duplicates)