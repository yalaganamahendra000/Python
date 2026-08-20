numbers=[1, 2, 3, 2, 4, 1, 5]
new_list=[]
answer_list=[]
for i in numbers:
    if i in new_list:
        answer_list.append(i)
    else:
        new_list.append(i)
    
print(len(answer_list))
