#1.Create a list of 5 numbers and add a new number at the end.
list=[1,2,3,4,5]
list.append(6)
print(list)
#2.Create a list of names and insert "Rahul" at index 2.
list=["vivek","ram","abhi"]
list.insert(2,"Rahul")
print(list)
#3.Given [10, 20, 30, 20, 40, 20], remove the first occurrence of 20.
list=[10,20,30,20,40,20]
list.remove(20)
print(list)
#4.Given [5, 2, 8, 1, 9], sort the list in ascending and descending order.
list = [5, 2, 8, 1, 9]

list.sort()
print(list)

list.reverse()
print(list)
#5.Given [10, 20, 30, 40, 50], remove the last element and print the removed element.
list=[10, 20, 30, 40, 50]

print(list.pop())
#6.Given [1, 2, 2, 3, 2, 4], find how many times 2 occurs.
list=[1, 2, 2, 3, 2, 4]
print(list.count(2))
#7.Given ["apple", "banana", "mango", "orange"], find the index of "mango".
list=["apple", "banana", "mango", "orange"]
print(list.index("mango"))
#8.Create two lists and combine the second list into the first using extend().
list_a=[1,2,3,4]
list_b=[5,6,7,8]
list_a.extend(list_b)
print(list_a)
#9.Create a tuple (10, 20, 10, 30, 10, 40) and find how many times 10 occurs.
tuple_a= (10, 20, 10, 30, 10, 40)
print(tuple_a.count(10))
#10.Given the tuple ("Python", "Java", "C++", "JavaScript"), find the index of "C++".
tuple_x= ("Python", "Java", "C++", "JavaScript")
print(tuple_x.index("C++"))