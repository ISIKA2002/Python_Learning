#match_cash_conditional
n1= int(input("Enter a n1 value:"))
n2= int(input("Enter a n2 value:"))
operater= input("Enter a operater:")
match operater:
        case "+":
            print("n1 + n2:", n1+n2)
        case "-":
            print("n1 - n2:", n1-n2)
        case "*":
            print("n1 * n2:", n1*n2)
        case _:
            print("Invalid operater")        