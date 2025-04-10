def calculate(user):
    if user % 2== 0 :
       return "even"
    else: 
        return "odd"

user = int(input("Enter your number: "))

result = calculate(user)
print(f"Your number : {user} is {result}")