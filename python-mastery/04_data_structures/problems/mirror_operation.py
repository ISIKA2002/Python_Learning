#Given a string and a number N, we need to mirror the characters from the N-th position up to the length 
#of the string in alphabetical order. In mirror operation, we change 'a' to 'z', 'b' to 'y', and so on.
'''a1=["a", "b", "c"]
b1=["z", "x", "y"]
dict1= (zip(a1,b1))
dict2= set(dict1)
print(dict2)'''
#n=3
#str=possible

input_str= input("Enter string:")
n = int(input("Enter n:"))
alpha="abcdefghijklmnopqrstuvwxyz"
reverse_alpha= alpha[::-1]
dict1= dict(zip(alpha,reverse_alpha))

#Find the part of string on which we will do mirror operation
prefix= input_str[0:n-1]
suffix= input_str[n-1:]

#finding the mirror string
mirror=""
for i in range(0, len(suffix)):
    mirror = mirror + dict1[suffix[i]]

#creating the final string
res = prefix + mirror
print("Result:", res)
