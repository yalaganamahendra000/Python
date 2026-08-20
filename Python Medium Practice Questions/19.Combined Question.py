sentence="Python is easy and Python is powerful"
sentence=sentence.split()
count=0
for i in range(len(sentence)):
    if(sentence[i]=="Python"):
        count=count+1

print(count)