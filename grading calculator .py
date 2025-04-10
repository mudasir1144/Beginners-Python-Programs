marks= int(input("What's your numbers: "))

def calculate_grade(marks):

    if  marks  >=90 :
        return("Grade A")
    elif marks >=80 :
        return("Grade B")
    elif marks >=70:
        return("Grade C")
    elif marks >=60:
        return("Grade D")
    else:
        return("Grade F")

def main():
    if 0 <= marks <= 100:
        marks = calculate_grade(marks)
        print("Your grade is : {marks}")

    else:
        print("Enter value in between 0 to 100 only")
main()