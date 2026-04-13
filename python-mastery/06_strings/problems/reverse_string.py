#Reverse string
def rev_string(str):
    rev= str[::-1]
    return rev

str= input("Enter the string:")
reversed_str= rev_string(str)
print("Reversed string is:", reversed_str)