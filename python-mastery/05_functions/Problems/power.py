'''Make a function which calculates 'a' raised to the power 'b' using recursion.
Input:a = 2, b = 3, Formula:a^b, Output:a raised to power b = 8'''
def power_of_ab(a,b):
    if b==0:
        return 1

    res= a * power_of_ab(a,b-1)
    return res

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

ans= power_of_ab(a,b)
print("Result is:", ans)