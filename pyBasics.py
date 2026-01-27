print("hello")
a1=float(input("Enter first number"))
a2 = float(input("Enter second number"))
a= int(input("1 for Addition\n 2 for substraction \n 3 for multiplication\n 4 for division"))
print("Answer is ")
if a==1:
    print(a1+a2)
elif a ==2:
    print(a1-a2)
elif a == 3:
    print(a1*a2)
elif a == 4:
    print(a1//a2)
