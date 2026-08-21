#Given a list of numbers, find the second-largest element.
numbers = [10, 25, 8, 40, 15]

largest = numbers[0]
second_largest = numbers[0]

for i in numbers:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print(second_largest)