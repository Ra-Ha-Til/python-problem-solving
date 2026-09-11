is_logged_in = int (input("Are you logged in? (0/1)"))
is_verified = int (input("Are you verified?(0/1)"))
is_admin = int(input("Are you admin?(0/1)"))

if is_logged_in == 1 :
    if is_verified == 1:
        if is_admin == 1:
            print("Admin Banking Access")
        else:
            print("Customer Banking Access")

    else:
        print("Verification Required")
else:
    print("Please Login")