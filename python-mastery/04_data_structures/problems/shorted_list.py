#Give 3 array, find common elements in 3 shorted list using sets
l1=[1,2,3,4,5,6]
l2=[3,4,5,6,7,8]
l3=[4,5,6,7,8,9]

s1= set(l1)
s2= set(l2)
s3= set(l3)

s4= (s1, s2, s3)
print(s4)

#use intersection() function to store the value in new set
s1s2=s1.intersection(s2)
print("Updated set:", s1s2)
final_values=s1s2.intersection(s3)
print("final values is:", final_values)
print ("Datatype is:", type(final_values))