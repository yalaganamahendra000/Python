#Given a list, create a new list containing only the even numbers.
numbers=[1,2,3,4,5,6,7,8]
new_list=[]
for i in numbers:
    if(i%2==0):
        new_list.append(i)
print(new_list)
