import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
run_again='n'
run=1
print(logo)

def calculator(number1,number2,operation):
    while(operation!='+' and operation!='-' and operation!='x' and operation!='/'):
        operation=input("Invalid operation, type again:")
    
    if operation=='+':
        return number1+number2
    elif operation=='-':
        return number1-number2
    elif operation=='x':
        return number1*number2
    else:
        return number1/number2
        

while(run):

    if run_again=='n':
        number1=float(input("What's the first number? "))
    else:
        number1=result

    operation=input("What's the operation? '+','-','x','/' ")
    number2=float(input("What's the other number? "))

    result=calculator(number1,number2,operation)

    print(f"{number1} + {number2} = {result}")

    run_again=input(f"Type 'y' to continue calculating with {result}, or 'n' to star a new calculation or press Enter to finish: ").lower()
    if run_again=="":
        run=0
    elif run_again=='n':
        os.system("clear")