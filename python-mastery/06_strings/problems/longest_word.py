#Count logest word
def longest_word(str):
    word= str.split()
    long_word= ""
    for i in word:
        if len(i) > len(long_word):
         long_word = i
    return long_word
    
str= input("Enter a string:")
result= longest_word(str)
print("Longest word:", result)
