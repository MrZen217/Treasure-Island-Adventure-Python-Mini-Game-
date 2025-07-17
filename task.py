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
answer_1 = (input("Where do you wanna go is it\n Type 'left' or 'right' \n").lower())

if answer_1 == "left":
    answer_2 = (input("You've come to a lake. There is an island in the middle of the lake.\n "
                "Type 'wait' to wait for the boat. Or type 'swim' to swim across\n").lower())

    if answer_2 == "wait":
        answer_3 = (input("Congrats you arrive in the island. And you see there are three cave in the island\n"
                          "Choose what cave you will enter: 'blue' 'red' 'yellow'\n").lower())

        if answer_3 == "blue":
           print("GAME OVER WRECK BY BEAR ! ! !")

        elif answer_3 == "yellow":
           print(" CONGRATULATION YOU GET THE ONE PIECE ! ! !")

        else:
           print("GAME OVER BITTEN BY SNAKE ! ! !")

    else:
        print("YOU DIE BY DROWNING THE WAVE IS TO HIGH ! ! !")
else:
    print("YOU DIE BECAUSE OF STARVATION ! ! !")

