import os
import time

logo="""

   _____       __  __                     
  / ____|     / _|/ _|                    
 | |     ___ | |_| |_ ___                 
 | |    / _ \|  _|  _/ _ \                
 | |___| (_) | | | ||  __/                
  \_____\___/|_| |_| \___|   _            
    |  \/  |          | |   (_)           
    | \  / | __ _  ___| |__  _ _ __   ___ 
    | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \\
    | |  | | (_| | (__| | | | | | | |  __/
    |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|
                                          
                                          
"""
drinks={
    "latte":{
        "money":2.50,
        "water":200,
        "milk":150,
        "coffee":24
    },
    "espresso":{
        "money":1.50,
        "water":50,
        "milk":0,
        "coffee":18,
    },
    "cappuccino":{
        "money":3.0,
        "water":250,
        "milk":100,
        "coffee":24
    }

}
ingredients={
    "water":300,
    "milk":200,
    "coffee":100,
    "money":0
}

aux=3
invalid=0
change=0
turn_on="off"
run=1

def money_count(quarters,dimes,nickles,pennies):
    pay=(quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    return pay

while(turn_on!=""):
    turn_on=input("Press Enter to turn on the machine!!")
    os.system('clear')

print("Turning on.")
time.sleep(1)
os.system('clear')
print("Turning on..")
time.sleep(1)
os.system('clear')
print("Turning on...")
time.sleep(1)
os.system('clear')
print(logo)

while(run):

    option=input("\nWhat would you like?? (Espresso/latte/Cappuccino):").lower()
    os.system('clear')

    while(option!="espresso" and option!= "latte" and option!="cappuccino" and option!="refill" and option!="report" and option!="exit"):
        option=input("Invalid option, try again: ").lower()

    if(option=="refill"):
        ingredients["water"]=300
        ingredients["milk"]=200
        ingredients["coffee"]=100
        print("Machine refueled!!")
    elif(option=="report"):
        print("")
        for i in ingredients:
            if i=="water" or i=="milk":
                print(f"{i.title()}: {ingredients[i]}ml")
            elif i=="coffee":
                print(f"{i.title()}: {ingredients[i]}g")
            else:
                print("%s: R$ %.2f"%(i.title(),ingredients[i]))
    elif(option=="exit"):
        run=0
    else:
        for i in ingredients:
            if ingredients[i]<drinks[option][i] and i!="money" :
                invalid=1      
        if invalid==0:
            print("Please insert your coins.")
            quarters=int(input("How many quarters?: "))
            dimes=int(input("How many dimes?: "))
            nickles=int(input("How many nickles?: "))
            pennies=int(input("How many pennies?: "))
            print()
            pay=money_count(quarters,dimes,nickles,pennies)
        if pay<drinks[option]['money']:
            print("Not enough money, sorry")
            print(f"You need {drinks[option]['money']-pay} more dollars")
        elif invalid==1:
            print("Not enough ingredients")   
        else:
            while(aux>0):
                print("Bzz..", flush=True,end="")
                aux-=1
                time.sleep(1)
            print(f"\nHere is your {option}")
            if pay>drinks[option]['money']:
                change= pay-drinks[option]['money']
                print(f"Your change R$:{change}")
            for i in ingredients:
                ingredients[i]= ingredients[i] - drinks[option][i]

    aux=3
    invalid=0
    ingredients['money']= ingredients['money']*-1