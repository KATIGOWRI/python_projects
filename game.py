print(r'''
*******************************************************************************
          |                   |                  |                     |le
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

start = input("This is the starting point. You have two options: Left or Right. Please enter your choice: ").lower()

if start == "left":
    print("You're in stage 2.")
    next_stage = input("Congratulations! You're in stage 2. Choose again: Left or Right: ").lower()
    
    if next_stage == "left":
        print("You're in stage 3.")
        next_stage1 = input("Congratulations! Final stage. Choose again: Left or Right: ").lower()
        
        if next_stage1 == "right":
            print("You fell into a river and died. Game over!")
        elif next_stage1 == "left":
            print("🎉 You found the treasure! YOU WIN! 🎉")
        else:
            print("Invalid input. Game over!")
    elif next_stage == "right":
        print("You fell into a trap. Game over!")
    else:
        print("Invalid input. Game over!")

elif start == "right":
    print("You walked into a wall and lost the game.")
else:
    print("Invalid input. Game over!")
