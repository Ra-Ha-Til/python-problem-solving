balance = int(input("Enter your balance:"))
withdraw_amount = int(input("Enter your withdraw amount:"))

if balance <= 0:
    print("Account Inactive")

elif withdraw_amount <= 0:
    print("Invalid Amount")

elif balance < withdraw_amount:
    print("Insufficient Balance")

else:
    balance = balance - withdraw_amount 

    if withdraw_amount >=50000:
        print("Large Withdrawal")

    else:
        print("Withdrawal Successful")

    print("Remaining Balance:", balance)
