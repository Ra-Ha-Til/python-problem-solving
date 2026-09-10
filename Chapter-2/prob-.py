balance = int(input("Enter the amount:"))
withdraw = int (input("Enter the withdraw amount:"))

if withdraw <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")