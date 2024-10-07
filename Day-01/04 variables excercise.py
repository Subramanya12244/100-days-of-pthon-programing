# swap two variables

a=int(input("enter the value of the a:"))
b=int(input("enter the value of the b:"))

# temp=a
# a=b
# b=temp
a=a+b
b=a-b
a=a-b
print("after swapping")
print("the value of the a:",a)
print("the value of the b:",b)