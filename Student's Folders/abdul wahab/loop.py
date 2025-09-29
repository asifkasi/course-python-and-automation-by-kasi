# we need to write code take input from user
username = input("enter your username:")
password = int(input("enter your password:"))

username_value = "wahab1999"
password_value = 123456

if (username == username_value and password == password_value ):
    print("access granted")
elif (username != username_value and password == password_value):
    print("invalid username")
elif (username == username_value and password != password_value):
    print("Invalid password")
else:
    print("Access denied")
