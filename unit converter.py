def kilometer_to_miles(user):
    return user*0.62137
def miles_to_kilometer(user):
    return user/0.62137
def kilogram_to_pounds(user):
    return user*2.2
def pounds_to_kilogram(user):
    return user/2.2
def celsius_to_fahrenheit(user):
    return user*(9/5)+32
def fahrenheit_to_celsius(user):   
    return (user-32)*5/9

user = input("convert from \n1.Kilometer to miles \n2. Miles to kilometers \n3. Kilogram to pounds \n4. Pounds to kilogram \n5. Celsius to fahrenheit \n6. Fahrenheit to celsius \n7. Choose (1/2/3/4/5/6): ")

choice = int(input("Enter Your number: "))

if user == "1":
    result = kilometer_to_miles(choice)
    print(f"The converted value is: {result:.2f}")
elif user =="2":
    result= miles_to_kilometer(choice)
    print(f"The converted value is:{result:.2f}")
elif user =="3":
    result = kilogram_to_pounds(choice)
    print(f"The converted value is : {result:.2f}")
elif user =="4":
    result = pounds_to_kilogram(choice)
    print(f"The converted value is : {result:.2f}")
elif user =="5":
    result = celsius_to_fahrenheit(choice)
    print(f"The converted value is : {result:.2f}")
elif user =="6":
    result = fahrenheit_to_celsius(choice)
    print(f"The converted value is : {result:.2f}")
else: 
    print("Choose the valid number!")
