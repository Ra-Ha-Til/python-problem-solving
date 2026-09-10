balance = int (input("Enter your balance:"))
withdraw = int (input("Enter your withdraw:"))

if withdraw >0 and withdraw <= balance and balance > 0:
    print("Withdrawal successful")