#Tuple types
#create a tuple
colours= ("Black", "Green", "Yellow", "Pink")
print("Print tuple:", colours)

#creating a tuple with one item
fruit=("Apple",)
#or
fruits= tuple(("Apple"))

#check the type 
print("Typpe of the fruit is:", type(fruit))
print("Typpe of the fruits is:", type(fruit))
print("Type is", type(colours))
#check the length of the tuple
print("Length of the tuple:", len(colours))

#Accessing items in tuple
print("Access item [posetive indexing]:", colours[0]) #posetive indexing
print("Access item [Negative indexing]:", colours[-1]) #negative indexing
print("Access item:", colours[1:3]) #range of posetive indexing
print("Access item:", colours[-2:]) #range of negative indexing

#Checking if an item is present in a tuple 
if "Green" in colours:
    print("Green is present")

