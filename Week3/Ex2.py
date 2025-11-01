correct_password = "pass1234"
login_attempts = 3
successful_login = False

while login_attempts > 0:
    password = input("Enter you password: ")
    if password == correct_password:
        successful_login = True
        break
    login_attempts -= 1

if successful_login:
    print("Correct password, login is granted!")
else:
    print("You exceeded the maximum number of attempts. Try again later..")