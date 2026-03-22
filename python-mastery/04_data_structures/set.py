#Set types
#Creating a set
names = {"Sia", "Hira", "Yel"}
print("Set:", names)
print(len(names)) #length of the set
print(type(names)) #datatype of the set

#Access items of set
print("Access item of set:")
for x in names:
    print(x)

#Checking if an item exites in a set
if "Sia" in names:
    print("Sia is in the set")

#Adding elements to the set using **add() function**
names.add("Ria")
print("Added new elements to the set:", names)
names.add("Sia") #not add in the set because set donot allow duplicate elements
print("Added new elements to the set:", names)

#Adding another sequence in the set using **update() function**
name_list=["Pia", "Kia"]
names.update(name_list)
print("Adding another sequence in the set:", names)

#removing elements from set using **remove() function**
names.remove("Kia")
print("After remove element:", names)

#use of discard() function
#This fuction not thow an error if the item is not present in the set
names.discard("Lia")
print("After apply discard function:", names)

#Joining 2 sets
s1={'a', 'e', 'i'}
s2={'i', 'o', 'u'}
print("Join 2 sets:", s1, s2)
 
#using union() function to joining 2 sets
s3= s1.union(s2)
print("Join 2 steps using union function:", s3)

#If you want to add s2 set to add after s1 set end
s1.update(s2)
print("Add s2 after s1 set using update function:", s1)

#Keep only duplicates while joining using intersection_update() function
'''s1.intersection_update(s2)
print("Only show duplicate values using intersection_update function:", s1)'''

#Keep all values expect duplicates symmetric_difference_update() function
'''s1.symmetric_difference_update(s2)
print("Print all datas expect duplicates using symmertic_difference_duplicates function:", s1)'''