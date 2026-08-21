#.Write a recursive function to find the sum of numbers from 1 to n. Example: Input 5 → Output 15.

def sum_numbers(n):
    if n == 0:
        return 0

    return n + sum_numbers(n - 1)


print(sum_numbers(5))
