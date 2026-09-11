marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance: "))
family_income = int(input("Enter your family income: "))

if marks < 40:
    print("Result: Fail")
    print("Scholarship: Not Eligible")

else:
    if attendance < 75:
        print("Result: Attendance Shortage")
        print("Scholarship: Not Eligible")

    else:
        print("Result: Pass")

        if marks >= 90 and family_income <= 30000:
            print("Scholarship: 100%")

        elif marks >= 80 and family_income <= 50000:
            print("Scholarship: 50%")

        else:
            print("Scholarship: Not Eligible")