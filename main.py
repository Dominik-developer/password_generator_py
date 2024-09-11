import string
import random

def password():
  
    sLet = list(string.ascii_lowercase) 
    bLet = list(string.ascii_uppercase) 
    digits = list(string.digits) 
    specSymb = list(string.punctuation)  

    passwordSymbols = sLet + bLet + digits + specSymb

    passwordLenght = random.randint(6,10)

    generatedPassword = []

    for _ in range(passwordLenght):
        generatedSymbol = random.choice(passwordSymbols)
        
        generatedPassword.append(generatedSymbol)

    finalPassword = ''.join(generatedPassword)

    RED = '\033[91m'

    print('Your new password: '+f"{RED}" +finalPassword + "" )


def check():
    print('lets check this password')
 

def menu():
    print('Password generator \n')
    #print('Choose what do you want to do: ')
        
    try:   
        choice = int(input("To generate new password choose 1: "))

        if choice == 1:
            password()

        elif choice == 2:
            check()

        else:
            print('\nWrong data typed in, try again. \n')
            menu()

    except ValueError:
        print("Wrong data typed in or wrong number chosen, try again. \n")
        menu()



#start
menu()