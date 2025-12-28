a=float(input("Enter 1st number "))
b=float(input("Enter 2nd number "))

print("Operations to be perform:")
print("Addition '+'\nSubtraction '-'\nMultiplication '*'\nDivision '/'")

op=input("Enter operation ")

if op=="+":
    res=a+b
    print("Result: ",res)
elif op=="-":
    res=a-b
    print("Result: ",res)
elif op=="*":
    res=a*b
    print("Result: ",res)
elif op=="/":
    if a!=0:
        res=a/b
        print("Result: ",res)
    else:
        print("Zero not allowed in division")
else:
    print("Invalid Operation")
