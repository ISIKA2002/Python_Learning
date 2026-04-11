#Taking input
text= input("Enter a string:")

#Uppercase
print("Upper:", text.upper())

#Lowercase
print("Lower:", text.lower())

#Capitalize (first letter capital)
print("Capitalize:", text.capitalize())

#Title (each word capital)
print("Title:", text.title())

#Length of string
print("Length:", len(text))

#Count a character
ch= input("Enter a char to count:")
print("Character count:", text.count(ch))

#Find position of character
ch1= input("Enter the char to find:")
print("Index:", text.find(ch1))

#Replace word
old=input("Enter word to replace:")
new= input("Enter new word:")
print("Replace:", text.replace(old, new))

#Check startswith
start= input("Enter the start word:")
print("Start with:", text.startswith(start))

#Check endswith
end = input("Enter end word: ")
print("Ends with:", text.endswith(end))

#Split string
print("Split:", text.split())

#Join example
words = ["Python", "is", "easy"]
print("Join:", " ".join(words))

#Remove spaces
print("Strip:", text.strip())

#formart
student_n= "John"
roll_num= 100
s1= "Student name is {s} and roll number is {r}".format (s= student_n, r= roll_num)
print(s1)