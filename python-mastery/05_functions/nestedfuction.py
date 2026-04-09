#Nested function (function inside function)
def outerfunction():
    x=2
    def innerfunction():
        y=5
        result = x + y
        return result
    return innerfunction()
output= outerfunction()
print(output)

