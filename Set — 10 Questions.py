#1.Create a set of 5 numbers and add a new number using add()
set={1,2,3,4,5}
set.add(100)
print(set)
#2.Given {10, 20, 30, 40}, remove 30 from the set.
set={10,20,30,40}
set.discard(30)
print(set)
#3.Given {1, 2, 3} and {3, 4, 5}, find their union.
num_a={1,2,3}
num_b={3,4,5}
num_c=num_a.union(num_b)
print(num_c)
#4.Given {1, 2, 3, 4} and {3, 4, 5, 6}, find their intersection.
a={1,2,3,4}
b={3,4,5,6}
c=a.intersection(b)
print(c)
#5.Given {1, 2, 3, 4} and {3, 4, 5}, find the elements present only in the first set.
e1={1,2,3,4}
e2={3,4,5}
e3=e1.difference(e2)
print(e3)
#6.Given {1, 2, 3} and {2, 3, 4}, find the symmetric difference.
A={1,2,3}
B={2,3,4}
C=A.symmetric_difference(B)
print(C)
#7.Create a set containing duplicate values and remove all duplicates.
numbers={1,2,3,3,4,4,4,5,5,5,5,5,5,5,5,6,7}
print(numbers)
#8.Given two sets, check whether they have any common elements.
n1={1,2,3,4,5,6,7}
n2={4,5,6,7,8,9}
result=n1.isdisjoint(n2)
print(result)
#9.Create a set and remove all its elements using clear().
nums={1,2,3,4,5}
nums.clear()
print(nums)
#10.Given {10, 20, 30, 40}, check whether 20 exists in the set.
elements={10,20,30,40}
if 20 in elements:
    print("yes 20 exists in elements")