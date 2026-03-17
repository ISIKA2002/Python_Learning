#List types
#Create a list
fruits=["Mango", "Banana", "Apple"]

#Print the list
print(fruits)
#Print the type of list
print(type(fruits))
#Print the length of list
print(len(fruits))

#Checking if an item is present in the list
if "Banana" in fruits:
    print("Banana is present in the list")
#Checking if an item is not present in the list
if "Kiwi" not in fruits:
    print("Kiwi is not present in the list")

#Accessing items of a list
#Checking index
print(fruits[0]) #indexing
print(fruits[-1]) #negative indexing
print(fruits[1:3]) #range of indexes
print(fruits[-3:-1]) #range of negative indexes

#Adding elements to a list
#append() function
fruits.append("Kiwi")
print("After apply append function:", fruits)

#insert() function
fruits.insert(3, "Orange")
print("After apply insert function:", fruits)

#extend funtion
add_fruits= ["Papaya", "Grapes"]
fruits.extend(add_fruits)
print("After apply extend function:", fruits)

#Remove elements from a list
#remove() function
fruits.remove("Mango")
print("After apply remove function:", fruits)

#pop() function
fruits.pop() #by default last element is remove from the list
print("After apply pop function [by default remove last element]:", fruits)
fruits.pop(2)
print("After apply pop function: [2nd element remove]:", fruits)

#Changing item in a list
#At a index
fruits[1]="Pineapple"
print("After change the index:", fruits)

#In a range
fruits[1:3]=["Coconut"]
print("After change the item in a range:", fruits)

#Shorting a list
#Ascending 
fruits.sort() #by default ascending order
print("After apply sort function for ascending order", fruits)

#Descending
fruits.sort(reverse=True)
print("Descending order:", fruits)

#Reverse the list
fruits.reverse()
print("After apply reverse function:", fruits)

# Loop through list
print("List elements:")
for i in fruits:
    print(i)

#List comprehension
new_fruits=[fruit for fruit in fruits if "a" in fruit] #syntax: [expression for item in list if condition]
print("Fruits containing 'a' new list:", new_fruits)

#Nested list
fruits.insert(3, ["Pear", "Litchi"])
print("Print the final list:", fruits)
print("Print the list between list:", fruits[3])
print("Print the element from the list between list:", fruits[3][1])