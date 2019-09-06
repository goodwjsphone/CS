# input a number between 1 and 10 and output the times table up to 12

num1 = int(input("Input a number between 1 and 10 "))
# print times table
x = 0
while x==0:

    if num1 <= 10:
        for i in range(1, 13):
            print (num1 * i)
            i + 1
            x= x+1
    
    # number is wrong print error
    else:
        print("That is not a number betweeen 1 and 10")
        num1 = input("Input a correct number ")
