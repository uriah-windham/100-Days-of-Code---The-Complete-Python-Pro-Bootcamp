print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You've come to a crossroads. Where would you like to go?")
direction = input("    Type \"left\" of \"right\"\n").lower()

if direction == "left":
    print("While walking down the dirt path, you fall into a hole and die. \n    GAME OVER.")

elif direction == "right":
    print("You come across a large lake. Will you walk around it or Swim across it?")
    lake_action = input("    Type \"walk\" or \"swim\"\n").lower()

    if lake_action == "swim":
        print("Once you make it to the middle of the lake, you grow exhausted and drown. \n    GAME OVER.")

    elif lake_action == "walk":
        print("You walk around the lake and come across three different houses.")
        print("One red, one blue, and one yellow. Which one will you go inside?")
        house_choice = input("").lower()

        if house_choice == "red":
            print("Once you go inside, the house catches flames and you burn inside. \n    GAME OVER.")

        elif house_choice == "yellow":
            print("You go inside, and after a short moment of catching your breath, the house is filled with poisonous gas, suffocating you. \n    GAME OVER.")

        elif house_choice == "blue":
            print("Once inside, you find a large chest of treasure. Congratulations. \n    YOU WIN.")

else:
    print("WRONG INPUT! YOU LOSE!")