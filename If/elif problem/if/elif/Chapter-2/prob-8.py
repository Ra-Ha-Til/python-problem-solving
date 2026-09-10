user = int (input("Enter your age:"))

if user>60:
    print("Age verification required")
elif user >= 18:
    print("Eligible to drive")
else:
    print("Not eligible to drive")