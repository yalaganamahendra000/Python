#Given a dictionary containing student names and marks, calculate the average marks.
students={"mahendra":79,"sai":75,"manoj":89}
sum=0
count=0
for marks in students.values():
    sum=sum+marks
    count=count+1
print(sum/count)
