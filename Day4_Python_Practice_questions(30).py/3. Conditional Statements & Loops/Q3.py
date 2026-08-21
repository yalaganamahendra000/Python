#Take a number and find the sum of its digits.
num=int(input())
sum=0
while(num>0):
    
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)
