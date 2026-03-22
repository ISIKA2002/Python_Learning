#Give 3 array, find common elements in 3 shorted list using sets
l1=[1,2,3,4,5,6]
l2=[3,4,5,6,7,8]
l3=[4,5,6,7,8,9]

s1= set(l1)
s2= set(l2)
s3= set(l3)

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)

#use intersection() function to store the value in new set
s1s2=s1.intersection(s2)
print("Common value of s1 and s2 sets:", s1s2)
final_values=s1s2.intersection(s3)
print("Final common values are:", final_values)
print ("Datatype is:", type(final_values))