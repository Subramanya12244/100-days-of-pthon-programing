print("Welcome to Treasure Island.Your mission is to find the treasure.")
level1=input("wheather you want to go Right or Left: ")
if level1=="Left":
    print("Fall into hall, Game Over!")
else:
    level2=input("Swim or Wait for Boat: ")
    if level2=="Swim":
        print("attacked by trout.Game Over.")
    elif level2=="Wait":
        print("you have survived and going for next level of the game.")
        level3=input("Which door you want to go \n1.Red \n2.Blue \n3.Yellow \n")
        if level3=="Red":
            print("You have been burnt alive!!, Game Over")
        elif level3=="Blue":
            print("You Have been eaten by the beasts!!, Game Over")
        elif level3=="Yellow":
            print("Congratulations!!, You have been Successfully Won the Treasure Hunt")
        else:
            print("You did not choose any door, Game Over")