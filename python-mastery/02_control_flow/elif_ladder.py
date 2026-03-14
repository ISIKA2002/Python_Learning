#elif_ladder_conditional
mark= int(input("Enter the mark:"))
if mark >= 90:
    print("Grade A")
elif mark >= 80:
    print("Grade B")
elif mark >= 70:
    print("Grade C:")
elif mark >= 60:
    print("Grade D") 
elif mark >= 50:
    print("Grade E") 
elif mark >= 40:
    print("Grade F") 
elif mark >= 30:
    print("Grade G") 
else:
    print("Failed")          