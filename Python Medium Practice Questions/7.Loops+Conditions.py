number=input()
count=0

for i in range(len(number)):

    if int(number[i])%2==0:
        count=count+1
print(count)