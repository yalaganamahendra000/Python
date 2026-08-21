#Take a sentence as input and create a dictionary containing the frequency of each word. Example: "apple banana apple mango banana apple" → {"apple": 3, "banana": 2, "mango": 1}.
sentence=str(input())
sentence=sentence.split()
dic={}
for i in sentence:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1

print(dic)