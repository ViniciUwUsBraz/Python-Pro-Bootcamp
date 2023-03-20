import random

letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','&','*']

print("Welcome to the PyPassword Generator!")

nt_letters=int(input("How many letters would you like in your password?: "))
nt_numbers=int(input("How many numbers would you like in your password?: "))
nt_symbols=int(input("How many symbols would you like in your password?: "))


letters_in_pass=[]
numbers_in_pass=[]
symbols_in_pass=[]

random_number=0
password_size=nt_letters+nt_numbers+nt_symbols
password=[]
password_str=""

count_for_letters=nt_letters
count_for_numbers=nt_numbers
count_for_symbols=nt_symbols

def find_elements(nt,array_pass,array):
    for i in range(nt):
        random_number=random.randint(0,len(array)-1)
        array_pass.append(array[random_number])

find_elements(nt_letters,letters_in_pass,letters)
find_elements(nt_numbers,numbers_in_pass,numbers)
find_elements(nt_symbols,symbols_in_pass,symbols)

while(password_size>0):
    random_number=random.randint(1,3)
    if random_number==1 and count_for_letters>0:
        password.append(letters_in_pass[count_for_letters-1])
        count_for_letters-=1
        password_size-=1
    elif random_number==2 and count_for_numbers>0:
        password.append(numbers_in_pass[count_for_numbers-1])
        count_for_numbers-=1
        password_size-=1
    elif random_number==3 and count_for_symbols>0:
        password.append(symbols_in_pass[count_for_symbols-1])
        count_for_symbols-=1
        password_size-=1

password_str="".join(password)
print(password_str)