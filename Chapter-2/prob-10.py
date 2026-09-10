price = int(input("Enter the price:"))
is_member = int (input("Are you member? (1/0)"))

if price >=5000:
    if is_member == 1:
        print("30% Discount")
    else:
        print("20% Discount")
else:
    if price < 5000:
       if is_member == 1:
           print("10% Discount")
       else:
           print("No Discount")
