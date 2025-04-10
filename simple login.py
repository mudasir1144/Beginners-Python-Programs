def cridentials(username, password):
    if username == correct_username and password == correct_password:
        return "Login successful"
    else:
        return "Try again"

username = input("Enter your username: ")
password = input("Enter your password: ")

correct_username = "mudasir1134"
correct_password = "1234"

results = cridentials(username, password)
print(f"{results}")
