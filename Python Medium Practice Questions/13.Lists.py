numbers= [12, 5, 8, 21, 4, 15, 10]
max=numbers[0]
min=numbers[0]
sum=0
for i in range(len(numbers)):
    if numbers[i]>max:
        max=numbers[i]
    elif numbers[i]<min:
        min=numbers[i]
    sum=sum+numbers[i]
print(max)
print(min)
print(sum)
