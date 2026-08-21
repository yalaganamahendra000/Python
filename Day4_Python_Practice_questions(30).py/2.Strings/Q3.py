#Take a string and check whether it is a palindrome.
string=str(input())
start=0
end=len(string)-1
while(start<end):
    if(string[start]!=string[end]):
        print("Not palindrome")
        break
    
    
    start=start+1
    end=end-1
else:
    print("palindrome")
   

  




