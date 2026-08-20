person_age =int(input("enter ur age :"))
person_id=str(input("do you have id ?"))

if person_age>=18 and person_id.lower()=="yes":
    print("Allowed")
else:
    print("Not Allowed")
