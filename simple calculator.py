def add (a ,b):
    return a + b
def subtract(a , b):
    return a - b
def multiply(a , b):
    return a * b
def division(a , b):
    if b==0:
        return "Error! Division by zero"
    else:
        return a / b

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your 2nd number: "))

print("Select Operation: ")
print("1. Addition(+)")
print("2. Substraction(-)")
print("3. Multiplication(*)")
print("4. Division (/)")

choice = input("Choose the operation (1/2/3/4): ")

if choice == "1":
    result = add(num1, num2)
    print(f"Results are : {num1} + {num2} = {result}")
elif choice == "2":
    result = subtract(num1, num2)
    print(f"Results are : {num1} - {num2} = {result}")
elif choice == "3":
    result = multiply(num1, num2)
    print(f"Results are : {num1} * {num2} = {result}")
elif choice == "4":
    result = division(num1, num2)
    print(f"Results are : {num1} / {num2} = {result}")
else:
    print("Enter valid Choice")
   

