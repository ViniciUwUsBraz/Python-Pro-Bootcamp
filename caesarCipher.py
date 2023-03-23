alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
run=1
aux=0 

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

while(run):

    decoded_message=[]

    option=input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    while(option!="encode" and option!="decode"):
        option=input("Invalid option, type again: ").lower()

    message=input("Type your message: ").upper()
    shift=int(input("Type the shift number: "))

    if option=="encode":
        for i in message:
            if i.isalpha():
                if alphabet.index(i)+shift > (len(alphabet)-1):
                    new_shift= (alphabet.index(i)+shift)%26
                    decoded_message.append(alphabet[new_shift])
                else:
                    decoded_message.append(alphabet[alphabet.index(i)+shift])
            else:
                decoded_message.append(i)
    elif option=="decode":
        for i in message:
            if i.isalpha():
                    if alphabet.index(i) -shift < -26:
                        new_shift=int(((alphabet.index(i)-shift)*-1)%26)
                        decoded_message.append(alphabet[alphabet.index(i)-new_shift])
                    else:
                        decoded_message.append(alphabet[alphabet.index(i) -shift])
            else:
                decoded_message.append(i)

    print("".join(decoded_message))

    again=input("Do you want to continue? 'Yes' 'No' ").lower()
    if(again=="yes"):
        run=1
        print("\n\n\n")
    else:
        run=0
    
                
