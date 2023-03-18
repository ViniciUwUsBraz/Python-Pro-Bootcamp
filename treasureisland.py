import os
import time

logo='''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
print(logo)
time.sleep(2)
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
time.sleep(2)
print("Let's start ")
time.sleep(2)
os.system("clear")
time.sleep(1)
direction=input("What direction do you want to go?? 'Left', 'Right' or 'Straight': ").lower()

if(direction=='right' or direction=='straight'):
    time.sleep(1)
    print("You fall into a hole.")
    time.sleep(1)
    print("Game Over!!")
else:
    time.sleep(1)
    print("You face a flood")
    time.sleep(1)
    decision=input("Do you want to stay and wait or swim trought?? 'Wait' or 'Swim': ").lower()
    if(decision=='swim'):
        time.sleep(1)
        print("You decided to pass through but a trout attack you.")
        time.sleep(1)
        print("Game Over!!")
    elif(decision=='wait'):
        print("You waited and found a boat.")
        time.sleep(1)
        door=input("You cross the flood and see three doors. Which door you want to go?? The red one, the blue one or the yellow one?? 'Red', 'Blue', 'Yellow' or 'Wait outside': ").lower()
        if(door=='red'):
            time.sleep(1)
            print("You entered in a burned room and has been burned too!!\nGame Over!!")
        if(door=='blue'):
            time.sleep(1)
            print("You entered in a room full of beasts and were attacked!!\nGame Over!!")
        if(door=="yellow"):
            time.sleep(1)
            print("You enteder in a room filled with gold, and in the center you find a chest!!")
            open=input("Do you want to open the chest?? 'Yes' or 'No': ").lower()
            if(open=='yes'):
                print("When you open the chest you see a strong light coming him, and when you realise its a CHEST FILLED WITH TREASURE!!\nYou Win!!")
            else:
                print("You dont open the chest and come back only with the golden objects in the room!!\nAt least you don lose!!")
        if(door=='wait'):
            print("You stand outside and starve yourself to the death!!\nGame Over!!\n'Why did you do that??'")

time.sleep(1)

