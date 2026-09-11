N = int(input("Enter the number:"))
if N >0:
    if N % 2 ==0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif N < 0 :
    if N % 2 ==0:
        print("Negative Even")
    else:
        print("Negative Odd")
else:
    print("Zero")