from myio import io as io
data = io.get_database()

def register_new_usr():
    registering = True
    new_user = {}
    new_user['balance'] = 0
    new_user['transactions'] = ""
    while(registering):
        new_user['first_name'] = input("Enter your first name\n").capitalize()
        new_user['last_name'] = input("Enter your last name\n").capitalize()
        creating_user_name = True
        while(creating_user_name):
            user_name = input("Enter a username\n")
            unique = True
            for p in data["users"]:
                if (user_name.lower() == p['user_name']):
                    print("Username already exists\n")
                    unique = False
                    break
            if (unique):
                creating_user_name = False
        new_user['user_name'] = user_name.lower()
        creating_pass = True
        while(creating_pass):
            password = input("Enter a password\n")
            confirm_pass = input("Confirm your password\n")
            if (password != confirm_pass):
                print('Password does not match\n')
            else:
                new_user['password'] = password
                creating_pass = False
        confirm_user = ''
        while (confirm_user != 'yes' and confirm_user != 'no'):
            confirm_user = input("Here is your user information:\n\tFirst Name: " + new_user['first_name'] + "\n\tLast Name: " + new_user['last_name'] + "\n\tUser name: " + new_user['user_name'] + "\nCofirm new user? Yes/No\n")
            if (confirm_user.lower() != "yes" and confirm_user.lower() != "no"):
                print("Please enter a valid request\n")
            else:
                if (confirm_user.lower() == "yes"):
                    registering = False

    data['users'].append(new_user)
    return "New user created"

def login():
    matched = False
    user_name = input("Enter your username\n")
    password = input("Enter your password\n")
    for p in data["users"]:
        if (user_name.lower() == p['user_name'] and password == p['password']):
            matched = True
    if matched:
        return ["Successful login\n", p]
    else:
        return ["Incorrect username or password\n"]

def balance():
    print("balance")

def withdraw():
    print("withdraw")

def deposit():
    print("deposit")

def history():
    print("history")
