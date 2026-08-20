sentence="Python is very easy to Learn"
sentence=sentence.split()
count=0
for i in range(len(sentence)):
    for j in range(len(sentence[i])):
        if sentence[i][j]in "aeiou":
            count=count+1

print(count)
    