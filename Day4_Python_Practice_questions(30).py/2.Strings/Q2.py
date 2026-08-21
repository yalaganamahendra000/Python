#Take a string and print it in reverse without using a built-in reverse function.
string=str(input())
rev=""
for i in range(len(string)-1,-1,-1):
    rev=rev+string[i]
    
print(rev)
