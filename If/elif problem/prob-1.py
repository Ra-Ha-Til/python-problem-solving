"""User-এর কাছ থেকে একটি integer number input নাও।
যদি number টি 10-এর চেয়ে বড় হয়, তাহলে:

Number is greater than 10   print করবে।

যদি 10-এর চেয়ে বড় না হয়, কিছু print করার দরকার নেই।

Example

Input: 15

Output:  Number is greater than 10"""

#___________________________________Ans__________________________________

"""a = int(input("Enter your number:"))

if a>10:
    print("Number is greater than 10")"""


#____________________________Ques-2_____________________________________
"""User-এর কাছ থেকে একটি integer number input নাও।

যদি number 0-এর চেয়ে ছোট হয়, তাহলে print করবে:

Number is negative

Example Input:

-5

Expected Output:

Number is negative"""

#______________________________Ans-2________________________

"""number = int(input("Enter the number:"))

if number <0:
    print("Number is negative")"""


#__________________________________qUES-3________________

a = int (input("Enter the first number:"))
b = int (input("Enter the second number:"))

if a>b and a<100:
    print("A is greater than B and less than 100")