#Multi_conditional_using_and_and_or
eng_mark= int(input("Enter the English mark:"))
math_mark= int(input("Enter the Math number:"))
if eng_mark >= 80 and math_mark >= 80:
    print("Grade A")
elif eng_mark >= 80 or math_mark >= 80:
    print("Grade B")
else:
    print("Grade C")