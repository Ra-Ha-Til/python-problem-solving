balance = int(input("Enter the balance:"))
withdraw = int(input('Enter the withdraw:'))

if balance > 0:
    if withdraw > 0:
        if withdraw <= balance:
         print("Withdrawal successful")
        else:
         print("Insufficient balance")
    else:
       print("Invalid WIthdrawal")
else:
    if balance <=0:
        print("Account inactive")
