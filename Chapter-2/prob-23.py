years = int(input("Enter the years:"))
performance = int(input("Enter your performance"))

if years >= 5:
    if performance >=90:
        print("Outstanding")
    else:
        print("Experienced")
else:
    if performance >=90:
        print("High Potential")
    else:
        print("Needs Improvement")