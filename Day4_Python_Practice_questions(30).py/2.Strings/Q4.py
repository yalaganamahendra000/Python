#Take a sentence and find the longest word in it.
sentence=str(input())
sentence=sentence.split()
longest=sentence[0]
for i in sentence:
    if(len(i)>len(longest)):
        longest=i
print(longest)
