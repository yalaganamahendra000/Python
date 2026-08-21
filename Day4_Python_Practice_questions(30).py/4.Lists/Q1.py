#Given a list of numbers, find the largest and smallest element without using max() or min().
numbers=[1,2,3,4,5]
largest=numbers[0]
smallest=numbers[0]
for i in numbers:
    if(i>largest):
        largest=i
    if(i<smallest):
        smallest=i
print(largest)
print(smallest)