years = int(input("Enter your years:"))
performance = int(input("Performance Score:"))
is_manager = int(input("Are you manager? (0/1):"))

if years >= 3:
    if performance >= 80:
        if is_manager ==1 :
            print("Bnous: 20%")
        else:
            print("Bonus: 10%")
    else:
        print("No Bonus")
else:
    
     if performance >=90:
        print("Bonus:5%")
     else:
        print("No Bonus")
