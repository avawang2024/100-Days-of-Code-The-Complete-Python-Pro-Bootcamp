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
print("You're at a cross road. Where do you want to go?")
road_direction=input('Type "left" or "right"\n')
if road_direction=="left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    method=input('Type "wait" to wait for a boat. Type "swim" to swim across.')
    if method =="wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue.")
        door=input('Which colour do you choose?')
        if door=="red":
            print("red is bad, you died.")
        elif door=="yellow":
            print("congratulations!")
        elif door=="blue":
            print("You enter a room of beasts. Game Over.")
    elif method =="swim":
        print("wrong method, you died.")
    else:
        print("Wrong method")

elif road_direction=="right":
    print("wrong road_direction, you died.")
else:
    print("Wrong road_direction")

