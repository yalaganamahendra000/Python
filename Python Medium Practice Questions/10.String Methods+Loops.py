string="hello123"
count_vowel=0
count_consonants=0
count_digits=0
for i in range(len(string)):
    if(string[i] in "aeiou"):
        count_vowel=count_vowel+1
    elif(string[i] not in"aeiou" and not string[i].isdigit()) :
    
        count_consonants=count_consonants+1
    if string[i].isdigit():
        count_digits=count_digits+1

print(count_vowel)
print(count_consonants)
print(count_digits)
