user = str (input("Enter user name:"))
password = str (input("Enter the password:"))

if user == 'admin' and password == '1234':
    print("Login successful ")

else:
    print("Invalid username or password")