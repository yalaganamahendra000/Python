a={1,2,3,4,5}
b={3,4,5,9,10}
c= a.union(b)
print(c,len(c))





d={2,3,4,5,6}
e={7,8,4,5,2}
f=d.intersection(e)
print(f,len(f))



g={1,2,3,4,5}
h={1,5,7,8,0}
i=g.difference(h)
print(i,len(i))



j={1,2,3,4,5,6}
k={1,2,3,7,8,9}
l=j.symmetric_difference(k)
print(l,len(l))