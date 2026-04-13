#Remove spaces
def remove_spe(str):
    space=str.replace(" ", "")
    return space
str= input("Enter the strting:")
result= remove_spe(str)
print("Result is:", result)