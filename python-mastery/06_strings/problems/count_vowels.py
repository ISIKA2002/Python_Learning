#count volums
def count_vol(str):
    str= str.lower()
    vol= "aeiou"
    count=0
    for i in str:
      if i in vol:
        count= count+1
    return count

str= input("Enter a string:")
vol_count= count_vol(str)
print("Volume count:", vol_count)   