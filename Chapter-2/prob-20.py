age = int(input("Enter yor age:"))
income = int(input("Enter your income:"))
credit_score = int (input("Enter your credit score:"))

if age >= 21:
    if income >= 30000:
        if credit_score >= 700:
              if age >= 60:
                     if income >=50000: 
                          print("Loan Approved")
                     else:
                          print("Loan Rejected")
              else:
                 print("Loan Approved")
        else:
               print("Loan Rejected")
    else:
           print("Loan Rejected")

else:
       print("Loan Rejected")
   