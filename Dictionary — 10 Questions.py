#1.Create a dictionary containing a student's name, age, and marks and print each value.
student={
    "name":"mahendra",
    "age":23,
    "marks":80,

}
for key in student.keys(),student.values():
    print(key)
#2.Given {"name": "Rahul", "age": 20}, add a new key city.
studentx={"name": "Rahul", "age": 20}
studentx["city"]="hyd"
print(studentx)
#3.Given {"name": "Rahul", "age": 20}, update the age to 21.
student_y= {"name": "Rahul", "age": 20}
student_y["age"]=21
print(student_y)
#4.Given {"name": "Rahul", "age": 20, "city": "Hyderabad"}, remove the city key.
student_x={"name": "Rahul", "age": 20, "city": "Hyderabad"}
student_x.pop("city")
print(student_x)
#5.Given a dictionary, check whether a particular key exists.
record={"name": "Rahul", "age": 20, "city": "Hyderabad"}
if "city" in record:
    print("key exists")
#6.Given {"apple": 50, "banana": 30, "mango": 40}, print all the keys.
records_x={"apple": 50, "banana": 30, "mango": 40}
print(records_x.keys())
#7.Given {"apple": 50, "banana": 30, "mango": 40}, print all the values.
records_x={"apple": 50, "banana": 30, "mango": 40}
print(records_x.values())
#8.Given a dictionary, use items() to print every key and value.
records_x={"apple": 50, "banana": 30, "mango": 40}
print(records_x.items())
#9.Given {"a": 10, "b": 20, "c": 30}, find the sum of all values.
dict_a= {"a": 10, "b": 20, "c": 30}
sum=0
for i in dict_a.values():
    sum=sum+i
print(sum)
#10.Given a dictionary ‘students’ containing student names and marks, find the student who has the highest marks.
students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Sneha": 95,
    "Karan": 88
}
max=students["Rahul"]
student_name="Rahul"
for i in students:
    if students[i]>max:
        max=students[i]
        student_name=i
print(max)
print(student_name)
