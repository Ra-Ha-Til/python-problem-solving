marks = int (input("Enter your marks:"))
attendance = int(input("Enter your attendance:"))

if marks >= 40:
    if attendance >=75:
        print("Passed")
    else:
        print("Attendence Shortage")

else:
    print("Failed")