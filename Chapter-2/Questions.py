"""============================================================
CHAPTER 2 — CONDITION & DECISION MAKING
TYPE 2 — IF / ELSE
============================================================

Problem #1 — Greater Than 10
------------------------------------------------------------
Problem Statement:
Given an integer N, determine whether N is greater than 10.

Input:
A single integer N.

Output:
Print "Greater than 10" if N is greater than 10.
Otherwise, print "10 or less".

Example:
Input:
15

Output:
Greater than 10


============================================================

Problem #2 — Pass or Fail
------------------------------------------------------------
Problem Statement:
Given a student's marks, determine whether the student has
passed or failed.

A student passes if marks are greater than or equal to 40.

Input:
A single integer marks.

Output:
Print "Pass" if marks are greater than or equal to 40.
Otherwise, print "Fail".

Example:
Input:
65

Output:
Pass


============================================================

Problem #3 — Number Classification
------------------------------------------------------------
Problem Statement:
Given an integer N, determine whether it is positive,
negative, or zero.

Input:
A single integer N.

Output:
Print:
"Positive or Zero" if N is greater than or equal to 0.
"Negative" otherwise.

Example:
Input:
-8

Output:
Negative


============================================================

Problem #4 — ATM Withdrawal
------------------------------------------------------------
Problem Statement:
An ATM receives a withdrawal request and the customer's
current balance.

Determine whether the withdrawal can be completed.

A withdrawal is successful if the requested amount is less
than or equal to the available balance.

Input:
Two integers:
balance
withdraw

Output:
Print "Withdrawal successful" if the withdrawal amount is
less than or equal to the balance.

Otherwise, print "Insufficient balance".

Example:
Input:
50000
30000

Output:
Withdrawal successful


============================================================

Problem #5 — Login Authentication
------------------------------------------------------------
Problem Statement:
A system allows login only when both the username and
password are correct.

The correct username is "admin".
The correct password is "1234".

Input:
Two strings:
username
password

Output:
Print "Login Successful" if both credentials are correct.
Otherwise, print "Login Failed".

Example:
Input:
admin
1234

Output:
Login Successful


============================================================

Problem #6 — Shopping Discount
------------------------------------------------------------
Problem Statement:
An online store gives a discount based on the order amount.

If the order amount is greater than or equal to 5000,
the customer receives a 20% discount.

Otherwise, the customer receives no discount.

Input:
A single integer price.

Output:
Print "20% Discount" if price is greater than or equal to
5000.

Otherwise, print "No Discount".

Example:
Input:
6500

Output:
20% Discount


============================================================

Problem #7 — Electricity Usage
------------------------------------------------------------
Problem Statement:
An electricity company classifies customers based on their
monthly electricity usage.

If the customer uses more than 100 units, classify the usage
as high.

Otherwise, classify it as normal.

Input:
A single integer units.

Output:
Print "High Usage" if units are greater than 100.
Otherwise, print "Normal Usage".

Example:
Input:
150

Output:
High Usage


============================================================

Problem #8 — Driving Eligibility
------------------------------------------------------------
Problem Statement:
Determine whether a person is eligible to drive based on
their age.

Rules:
- Age greater than 60 → "Senior Driver"
- Age 18 to 60 → "Eligible"
- Below 18 → "Not Eligible"

Input:
A single integer age.

Output:
Print the appropriate classification.

Example:
Input:
25

Output:
Eligible


============================================================

Problem #9 — Bank Withdrawal Classification
------------------------------------------------------------
Problem Statement:
A bank wants to classify a withdrawal request.

Rules:
- If the withdrawal amount is greater than the balance,
  print "Insufficient balance".
- Otherwise:
    - If withdrawal is greater than 50000,
      print "Large transaction".
    - Otherwise, print "Withdrawal successful".

Input:
Two integers:
balance
withdraw

Output:
Print the appropriate message.

Example:
Input:
100000
70000

Output:
Large transaction


============================================================

Problem #10 — E-Commerce Discount System
------------------------------------------------------------
Problem Statement:
An online store calculates discounts based on order amount
and membership status.

Rules:

If price is greater than or equal to 5000:
    Member → 30% Discount
    Non-member → 20% Discount

If price is less than 5000:
    Member → 10% Discount
    Non-member → No Discount

Input:
Two values:
price
is_member (1 for member, 0 for non-member)

Output:
Print the appropriate discount.

Example:
Input:
6000
1

Output:
30% Discount


============================================================

Problem #11 — ATM Withdrawal Classification
------------------------------------------------------------
Problem Statement:
An ATM must classify a withdrawal request.

Rules:

If withdrawal is less than or equal to balance:
    If withdrawal is greater than 20000:
        print "Large withdrawal"
    Otherwise:
        print "Withdrawal successful"

If withdrawal is greater than balance:
    print "Insufficient balance"

Input:
Two integers:
balance
withdraw

Output:
Print the appropriate message.

Example:
Input:
50000
30000

Output:
Large withdrawal


============================================================

Problem #12 — Exam Result System
------------------------------------------------------------
Problem Statement:
A student passes an exam only if both marks and attendance
requirements are satisfied.

Rules:

If marks are greater than or equal to 40:
    If attendance is greater than or equal to 75:
        print "Passed"
    Otherwise:
        print "Attendance Shortage"
Otherwise:
    print "Failed"

Input:
Two integers:
marks
attendance

Output:
Print the appropriate result.

Example:
Input:
65
80

Output:
Passed


============================================================

Problem #13 — Bank Account System
------------------------------------------------------------
Problem Statement:
Determine whether a bank transaction can be completed.

Rules:

If balance is greater than 0:
    If withdrawal is greater than 0:
        If withdrawal is less than or equal to balance:
            print "Withdrawal successful"
        Otherwise:
            print "Insufficient balance"
    Otherwise:
        print "Invalid withdrawal"
Otherwise:
    print "Account inactive"

Input:
Two integers:
balance
withdraw

Output:
Print the appropriate message.

Example:
Input:
50000
20000

Output:
Withdrawal successful


============================================================

Problem #14 — User Permission System
------------------------------------------------------------
Problem Statement:
A system determines the type of access a user should receive.

Rules:

If the user is logged in:
    If the user is an admin:
        print "Admin Access"
    Otherwise:
        print "User Access"
Otherwise:
    print "Please Login"

Input:
Two integers:
is_logged_in (1 or 0)
is_admin (1 or 0)

Output:
Print the appropriate access message.

Example:
Input:
1
1

Output:
Admin Access


============================================================

Problem #15 — Authentication System
------------------------------------------------------------
Problem Statement:
A system checks whether a user can log in.

Rules:

If the account is active:
    If the username is correct:
        If the password is correct:
            print "Login Successful"
        Otherwise:
            print "Wrong Password"
    Otherwise:
        print "Wrong Username"
Otherwise:
    print "Account Inactive"

Input:
Three integers:
is_active (1 or 0)
is_username_correct (1 or 0)
is_password_correct (1 or 0)

Output:
Print the appropriate login status.

Example:
Input:
1
1
0

Output:
Wrong Password


============================================================

Problem #16 — Online Banking Access
------------------------------------------------------------
Problem Statement:
Determine what type of banking access a user receives.

Rules:

If the user is logged in:
    If the user is verified:
        If the user is an admin:
            print "Admin Banking Access"
        Otherwise:
            print "Customer Banking Access"
    Otherwise:
        print "Verification Required"
Otherwise:
    print "Please Login"

Input:
Three integers:
is_logged_in
is_verified
is_admin

Each value is either 1 or 0.

Output:
Print the appropriate access message.

Example:
Input:
1
1
0

Output:
Customer Banking Access


============================================================

Problem #17 — Online Shopping Access
------------------------------------------------------------
Problem Statement:
Determine whether a customer can place an online order.

Rules:

If the customer is logged in:
    If the customer has a delivery address:
        If the customer has a payment method:
            print "Order Placed"
        Otherwise:
            print "Add Payment Method"
    Otherwise:
        print "Add Delivery Address"
Otherwise:
    print "Please Login"

Input:
Three integers:
is_logged_in
has_address
has_payment

Each value is either 1 or 0.

Output:
Print the appropriate message.

Example:
Input:
1
1
1

Output:
Order Placed


============================================================

Problem #18 — Premium Shopping Offer
------------------------------------------------------------
Problem Statement:
Determine which offer a customer receives.

Rules:

If the customer is logged in:
    If the customer is a member:
        If purchase amount is greater than or equal to 10000:
            print "Premium Offer Unlocked"
        Otherwise:
            print "Regular Member Offer"
    Otherwise:
        print "Become a Member"
Otherwise:
    print "Please Login"

Input:
Three values:
is_logged_in
is_member
purchase_amount

Output:
Print the appropriate offer.

Example:
Input:
1
1
12000

Output:
Premium Offer Unlocked


============================================================

Problem #19 — Electricity Bill Classification
------------------------------------------------------------
Problem Statement:
Classify electricity usage based on units and membership.

Rules:

If units are less than or equal to 100:
    Member → "Low Usage Discount"
    Non-member → "Low Usage"

If units are greater than 100:
    Member:
        If units are less than or equal to 300:
            "Medium Usage Discount"
        Otherwise:
            "High Usage Discount"

    Non-member:
        If units are less than or equal to 300:
            "Medium Usage"
        Otherwise:
            "High Usage"

Input:
Two integers:
units
is_member

Output:
Print the appropriate usage classification.

Example:
Input:
250
1

Output:
Medium Usage Discount


============================================================

Problem #20 — Loan Eligibility
------------------------------------------------------------
Problem Statement:
Determine whether a person is eligible for a loan.

Rules:

Basic requirements:
- Age must be at least 21.
- Income must be at least 30000.
- Credit score must be at least 700.

Additional rule:
- If age is 60 or above, income must be at least 50000.

If all required conditions are satisfied:
print "Loan Approved"

Otherwise:
print "Loan Rejected"

Input:
Three integers:
age
income
credit_score

Output:
Print "Loan Approved" or "Loan Rejected".

Example:
Input:
35
40000
750

Output:
Loan Approved


============================================================

Problem #21 — Employee Bonus Eligibility
------------------------------------------------------------
Problem Statement:
Determine whether an employee receives a bonus.

Rules:

If years worked are at least 3:
    If performance is at least 80:
        If the employee is a manager:
            print "Bonus: 20%"
        Otherwise:
            print "Bonus: 10%"
    Otherwise:
        print "No Bonus"

If years worked are less than 3:
    If performance is at least 90:
        print "Bonus: 5%"
    Otherwise:
        print "No Bonus"

Input:
Three values:
years
performance
is_manager

Output:
Print the appropriate bonus.

Example:
Input:
5
85
1

Output:
Bonus: 20%


============================================================

Problem #22 — Employee Performance Classification
------------------------------------------------------------
Problem Statement:
Classify an employee based on experience and performance.

Rules:

If years of experience are at least 5:
    If performance is at least 90:
        print "Outstanding"
    Otherwise:
        print "Experienced"

If years of experience are less than 5:
    If performance is at least 90:
        print "High Potential"
    Otherwise:
        print "Needs Improvement"

Input:
Two integers:
years
performance

Output:
Print the appropriate classification.

Example:
Input:
6
95

Output:
Outstanding


============================================================

END OF TYPE 2
============================================================"""