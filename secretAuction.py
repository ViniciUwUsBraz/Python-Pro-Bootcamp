import os
import time

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
                      
'''

run="yes"
peoples=[]
max=0
winner=""

print(logo)

def add_information(name,value):
    informations={
        "name":name,
        "value":value
    }
    peoples.append(informations)

time.sleep(1)
while(run=="yes"):
    name=input("What is your name? ")
    value=float(input("What is a bid? R$"))
    add_information(name,value)
    run=input("Are there any other bidders? ").lower
    time.sleep(1)
    os.system("clear")

for people in peoples:
    if people["value"]>max:
        max=people["value"]
        winner=people["name"]

print(f"The winner is {winner} with a bid of ${max:.2f} .")