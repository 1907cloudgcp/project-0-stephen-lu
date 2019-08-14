from service import service as s

def run_app():
    user = 0
    while (user != '1' and user != '2'and user != '3'):
        user = input("What would you like to do? (Enter a number):\n\t1. Register as a new user\n\t2. Login\n\t3. Exit\n")
        if user != '1' and user != '2' and user != '3':
            print("Please enter a valid request\n")
    if user == '1':
        print(s.register_new_usr())
    elif user == '2':
        login = s.login()
        print(login[0])
        if login[0] == "Successful login\n":
            logged_in = True
            while(logged_in):
                user = input("What would you like to do? (Enter a number):\n\t1. View Balance\n\t2. Withdraw\n\t3. Deposit\n\t4. View History\n\t5. Log out\n")
                if user != '1' and user != '2' and user != '3' and user != '4' and user != '5':
                    print("Please enter a valid request\n")
                elif  user == '1':
                    s.balance(login[1])
                elif  user == '2':
                    s.withdraw(login[1])
                elif  user == '3':
                    s.deposit(login[1])
                elif  user == '4':
                    s.history(login[1])
                elif  user == '5':
                    login = None
                    logged_in = False
    elif user == '3':
        s.exit_app()
        return False
    return True
