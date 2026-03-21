int(input("Enter your marks: "))

if marks < 34:
    print("Fail")
elif marks > 34 and marks<= 50:
    print("D")
elif marks > 50 and marks<= 70:
    print("C")
elif marks > 70 and marks<= 90:
    print("B")
elif marks > 90:
    print("A")