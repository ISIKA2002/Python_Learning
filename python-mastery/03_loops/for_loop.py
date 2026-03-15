#using for loop
#using only ending
print("Using end only:")
for i in range(5):
    print(i)

#using only starting and ending
print("Using start and end:")
for i in range(1, 5): 
    print(i) #only print upto end-1

#using only starting, ending, and step
print("Using start, end, and step:")
for i in range(1, 10, 2):
    print(i)

#reverse loop
#using only starting, ending, and step(in decreasing order)
print("Using start, end, and step(in decreasing order)")
for i in range(10, 0, -2):
    print(i)