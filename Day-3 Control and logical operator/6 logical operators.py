# basically there are 4 different types of logical operators
#  AND- all the value to be true to put the resultant true
# OR -any one of the statements need to be true to put the output True
# NOT- it will reverse the expression 
height=int(input("enter your height in cms:"));
if height>120:
    print("Hurrey you can ride the rollercoaster")
    age=int(input("enter your age: "));
    if age>18:
        print("you have to pay $12")
    elif age>12 and age<18:
        print("you have to pay $7")
    else:
        print("you have to pay $5")
else:
    print("Sorry you can't ride")