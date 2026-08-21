#Take three numbers as input and print the largest number.
a=int(input())
b=int(input())
c=int(input())
if(a>c)and (a>b):
    print("a is larger")
elif(b>c) and(b>a):
    print("b is larger")
else:
    print("c is larger")
