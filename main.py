

def password():
    print('program is running ')
 

def menu():
    print('Password generator \n')
        
    try:   
        choice = int(input("To start write chose 1 "))

        if choice == 1:
            password()
        else:
            print("Wrong data typed in, try again. \n")
            menu()

    except ValueError:
        print("Wrong data typed in or wrong number chosen, try again. \n")
        menu()

#start
menu()