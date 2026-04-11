#A lambda function is a small, one-line anonymous function in Python used for simple operations.
#lambda arguments : expression

#Add two numbers
add = lambda a, b: a + b
print(add(2, 3))

#using map()
nums = [1, 2, 3, 4]
result = list(map(lambda x: x*2, nums))
print(result)

#Using filter()
nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)