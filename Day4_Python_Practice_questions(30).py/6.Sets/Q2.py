#Given a list of numbers, use a set to find all the duplicate elements.
list_a=[1,2,3,4,5,1,2]
new_set=set(list_a)
seen=set()
duplicates=set()
for i in list_a:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)
print(duplicates)