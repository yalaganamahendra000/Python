numbers=[4, 15, 8, 21, 3, 17]
new_array=[]
for i in range(len(numbers)):
    if numbers[i]>10:
        new_array.append(numbers[i])
print(new_array)
