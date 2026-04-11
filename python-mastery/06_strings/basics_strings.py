#Create strings
s1= 'String1 here'
s2= "Staring2 here"
s3= '''Staring3
here'''
print(s1, s2, s3)
print(type(s1))
print(type(s2))
print(type(s3))

#Indexing in a string
print(s1[0])
print(s1[-1])

#Traversing a string
#using for loop
for i in s1:
    print(i)

#Using list comprehension
list = [char for char in s1]
for i in list:
    print(i)