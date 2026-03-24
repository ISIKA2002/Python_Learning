#Dictionary types
#Creating a dictionary
dic= {"John": 82678900023,
      "Riya": 68900087234,
      "Joy": 76543218907}

#Print the dict
print("Dictionary:", dic)
#Datatype of the dictionary
print(type(dic))
#Length of the dictionary
print(len(dic))

#Accessing item of dict
print("Accessing an item:",dic["John"])
print("Value showing using get() function:", dic.get("John"))

#If want to print all keys present in dict
print("Print all key:", dic.keys())

#Updating dict values
dic["John"]= 65748
print("Updated the key value:", dic)

#Adding element to the dict
dic["Ruhi"]= 8976099
print("Adding elements:", dic)

#Adding new dict keys in old dict
new_dic= {"Jos": 987654}
dic.update(new_dic)
print("Add new dict to the old one:", dic)

#Removing element to the dict
dic.pop("Riya")
print("After remove/pop:", dic)

#To remove the last added item
dic.popitem()
print("Remove last added item:", dic)

#To empty the dict
'''dic.clear()
print("After clear:", dic)'''

#To print the key of the dict
print("Only shows the key:")
for x in dic:
    print(x)

#To print the values of the dict
print("Only shows the values:")
for x in dic:
    print(dic[x])

#To print both values and keys of the dict
print("Print both values and keys:")
for x in dic.items():
    print(x)

#To print both values and keys in diffent values of the dict
print("Print both values and keys separectly:")
for x,y in dic.items():
    print(x,y)

#Nested dictionary
dict = {
    "Area1" :
        { "a" : 2,
          "b" : 3,
          "c" : 4
        },
    "Area2": 
    {
           "A" : 4,
           "B" : 6,
           "C" : 8
    }
} 
print(dict["Area1"]["a"])
print(dict["Area2"]["A"])