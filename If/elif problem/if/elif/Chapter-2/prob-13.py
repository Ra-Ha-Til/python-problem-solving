is_logged_in = int(input("Is logged in? (0/1)"))
is_admin = int(input("Is admin or normal user? (0/1)"))

if is_logged_in ==1:
    if is_admin == 1:
        print("Admin Access")
    else:
        print("User Access")
else:
    
     print("Please Login")

