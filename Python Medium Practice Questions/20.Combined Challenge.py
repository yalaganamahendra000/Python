numbers = [10, 25, 30, 45, 50, 75, 90, 100]
new_list=[]
for i in range(len(numbers)):
    if(numbers[i]>30 and numbers[i]%5==0 and numbers[i]!=75 ):
        new_list.append(numbers[i])

print(new_list)