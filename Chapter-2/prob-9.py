balance = int (input("Enter your balance:"))
withdraw = int (input("Enter your withdraw amount:"))

if withdraw <= balance:
    if withdraw > 50000:
        print("Large transaction")
    else:
        print("Withdrawal successful")
elif withdraw > balance:
    print("Insufficient balance")
