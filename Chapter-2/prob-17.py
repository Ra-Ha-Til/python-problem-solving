is_logged_in = int (input("Are you logged in? (0/1)"))
has_address = int (input("Please give your address: (0/1)"))
has_payment = int (input("Payment ? (0/1)"))

if is_logged_in == 1:
    if has_address == 1:
        if has_payment == 1:
            print("Order Placed")
        else:
            print("Add Payment Method")
    else:
        print("Add Delivery Address")
else:
    print("Please Login")