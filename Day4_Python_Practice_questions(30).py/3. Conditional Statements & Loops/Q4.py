#Take a number and check whether it is a prime number.
num=int(input())
if(num<2):
    print("not prime")
for i in range(2,num):
    if(num%i==0):
        print("not prime")
        break

else:
    print("prime")
