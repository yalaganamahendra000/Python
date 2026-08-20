words = ["apple", "banana", "kiwi", "orange", "grape"]

new_list=[]
for i in range(len(words)):
    if(len(words[i])>5):
        new_list.append(words[i])

print(new_list)