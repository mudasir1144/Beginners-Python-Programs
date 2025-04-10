def categorize_age(age):
    if age >=0 and age <=12:
        return "Child"
    elif age >=13 and age <=19:
        return "teenager"
    elif age >=20 and age <=59:
        return "Adult"
    elif age >=60:
        return "Senior"
    else:
        print("Enter valid age")

age  = int(input("Enter your age:"))

result= categorize_age(age)
print(f"Your age is: {age} and your are a: {result}")