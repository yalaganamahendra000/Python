#Take a string as input and count the number of vowels in it.
string=str(input())
string.lower()
count=0
for i in string:
    if i in "aeiou":
        count=count+1
print(count)