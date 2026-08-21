#Given a tuple of numbers, find the sum, maximum, and minimum values.
numbers=(1,2,3,4,5)
sum=0
max=numbers[0]
min=numbers[0]
for i in numbers:
    sum=sum+i
    if(i>max):
        max=i
    if(i<min):
        min=i
print(max)
print(min)
print(sum)