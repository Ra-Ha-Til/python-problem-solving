#________________Real World ATM withdrawal__________________________
balance = int (input("Enter the Balance:"))
withdraw = int (input("Enter the withdraw amount:"))

if withdraw < balance:
    print("Withdrawal successful")