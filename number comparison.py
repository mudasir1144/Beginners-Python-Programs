def compare(num1 , num2):
    if num1 >num2:
        return f"{num1} is greater than {num2}"
    elif num1 < num2: 
        return f"{num1} is less than {num2}"
    else:
        return f"{num1} is equal to {num2}"
    
num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
results = compare(num1 , num2)
print(f"{results}")
