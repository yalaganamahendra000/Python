#Write a function find_largest(numbers) that takes a list of numbers and returns the largest number without using max().
def find_largest(numbers):
    largest = numbers[0]

    for i in numbers:
        if i > largest:
            largest = i

    return largest


numbers = [10, 25, 8, 40, 15]

print(find_largest(numbers))