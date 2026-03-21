#Reverse a tuple
#in_tuple=(1,2,3,4,5,6)
#User input reverse in list declaration
n=int(input("Enter the length of the list to create a tuple:"))
input_tuple = []
for i in range(n):
    elements = input()
    input_tuple.append(elements)
    in_tuple = tuple(input_tuple)
print("Before reverse:", in_tuple)
print(type(in_tuple))
list = []
for x in reversed(in_tuple):
    list.append(x)
out_tuple = tuple(list)
print("Reverse tuple:", out_tuple)

#Using user input reverser
elements= input("Enter tuple elements separated by space:")
tuple_items= tuple(elements.split())
print("Before reverse:", tuple_items)
rev_tuple_ele=tuple_items[::-1]
print("After reverse:", rev_tuple_ele)
