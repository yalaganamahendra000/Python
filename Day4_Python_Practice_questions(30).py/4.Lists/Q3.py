#Given [10, 20, 10, 30, 20, 40, 30], remove the duplicates and create a list containing only unique values.
numbers=[10, 20, 10, 30, 20, 40, 30]
new_list=[]
for i in numbers:
    if i in new_list:
        continue
    else:
        new_list.append(i)
print(new_list)