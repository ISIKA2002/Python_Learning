#Declaring variables and check datatypes

#string_variable
name= "John Stive"
print("Name of the student is:", name)
print(type(name))

#integer_variable
roll_number= 107
print("Roll number:", roll_number)
print(type(roll_number))

#float_variable
percentage= 80.5
print("Percentage:", percentage)
print(type(percentage))

#boolean _variable
is_male_student= True
print("Is he a male student:", is_male_student)
print(type(is_male_student))

#To print all data in one line
print("To print all data in one line:")
print(name, roll_number, percentage, is_male_student)
print("Name of the student is:" + name + " Roll number:", roll_number, " Percentage:", percentage, " is he a male student:", is_male_student)

#print expressions
print("His percentage is changed to:", percentage -0.1)

#print with separator
print("Print with separator")
print(name, roll_number, percentage, is_male_student, sep="-")
#or
x=1
y=2
z=3
print(x,y,z, sep="->")
