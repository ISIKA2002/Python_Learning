#Frequent words
sentence= input("Enter sentence:").split()
freq={}

for word in sentence:
    if word in freq:
        freq[word]+= 1
    else:
        freq[word] = 1
print(freq)    