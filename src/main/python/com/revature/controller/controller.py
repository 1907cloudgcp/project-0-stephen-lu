from service import service as s

def run_app():
    user = 0
    while (user != '1' and user != '2'):
        user = input("What would you like to do? (Enter 1 or 2):\n\t1. Register as a new user\n\t2. Login\n")
        if user != '1' and user != '2':
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
                    s.balance()
                elif  user == '2':
                    s.withdraw()
                elif  user == '3':
                    s.deposit()
                elif  user == '4':
                    s.history()
                elif  user == '5':
                    break
