# Write a program which takes in three numbers and outputs the highest.

num1 = int(input("First number "))
num2 = int(input("Second number "))
num3 = int(input("Third number "))

if num1> num2 and num1> num3:
    print(num1)
elif num2> num1 and num2> num3:
    print(num2)
else:
    print(num3)

## ACS - Comments required and show where end of the if statement is.
