sentence= "banana apple mango cherry"
sentence=sentence.split()
small=sentence[0]
for i in range(len(sentence)):
    if(sentence[i]<small):
        small=sentence[i]

print(small) 