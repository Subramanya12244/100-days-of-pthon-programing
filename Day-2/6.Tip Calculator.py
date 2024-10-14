print("welcome to the tip calculator");
val=float(input("What was the total bill?"))
percent=int(input("How much tip wou you like to give? 10,12 or 15"))
people=int(input("How many people to split the bill?"))
val=val+val*(percent/100)
spliting=val/people;
print(f"Each person should pay: {round(spliting,2)}")