is_logged_in = int (input("Are you logged in? (0/1):"))
is_member = int (input("Are you member? (0/1):"))
purchase_amount = int (input("Total purchase amount?"))

if is_logged_in ==1:
    if is_member ==1:
      if purchase_amount >= 10000 :
        print("Premium Offer Unlocked")
      else:
        print("Regular Member Offer")
    else:
       print("Become a Member")
else:
   print("Please Login")