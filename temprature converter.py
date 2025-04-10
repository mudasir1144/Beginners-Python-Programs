def main():
    choose = input("Convert from\n1. Celsius To fahrenheit \n2. Fahrenheit to celsius \n3. Choose (1 or 2): ")

    if choose == "1" :
         celsius = float(input("Enter the celsius temprature: "))
         result = celsius_to_fahrenheit(celsius)
         print(f"The temprature converted to fahrenheit is : {result:.2f}")
    elif choose == "2":
         fahrenheit = float(input("Enter the temprature in Celsius"))
         result = fahrenheit_to_celsis(fahrenheit)
         print(f"The temprature converted to celsius is : {result:.2f}")
    else:
         print("Choose the valid number")

def celsius_to_fahrenheit(celsius):
        return celsius*(9/5)+32
       
def fahrenheit_to_celsis(fahrenheit):
    return  (fahrenheit-32)*5/9

main()

    
