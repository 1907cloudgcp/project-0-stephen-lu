from myio import io as io
from error import error as e
import datetime
import logging

logging.basicConfig(filename='app.log', format='%(asctime)s - %(message)s')

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
                print('Passwords do not match\n')
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
    logging.warning('New user ' + new_user['user_name'] + ' created')
    return "New user created"

def login():
    user_name = input("Enter your username\n")
    password = input("Enter your password\n")
    return find_user(user_name, password)

def find_user(user_name, password):
    matched = False
    for p in data["users"]:
        if (user_name.lower() == p['user_name'] and password == p['password']):
            matched = True
            user = p
    try:
        if matched:
            logging.warning('User ' + user_name + ' logged in')
            return ["Successful login\n", user]
        else:
            raise e.IncorrectLogin
    except e.IncorrectLogin:
        logging.warning('User ' + user_name + ' incorrect log in')
        return ["Incorrect username or password\n"]

def balance(user):
    print("Current balace: " + str(user['balance']) + '\n')

def withdraw(user):
    running = True
    while(running):
        try:
            amount = input("Enter value for withdrawl: ")
            if int(amount) < 0:
                raise e.ValueTooSmallError
            elif int(amount) <= user['balance']:
                running = False
            else:
                raise e.ValueTooLargeError
        except e.ValueTooSmallError:
            print('Invalid Value\n')
        except e.ValueTooLargeError:
            print('Invalid Value\n')
    user['balance'] -= int(amount)
    print("Withdraw successful, current balance: " + str(user['balance']) + '\n')
    time = datetime.datetime.now()
    user['transactions'] += str(time) + '    Withdraw ' + amount + '\n'


def deposit(user):
    amount = input("Enter value for deposit: ")
    user['balance'] += int(amount)
    print("Withdraw successful, current balance: " + str(user['balance']) + '\n')
    time = datetime.datetime.now()
    user['transactions'] += str(time) + '    Deposit ' + amount + '\n'

def history(user):
    return user['transactions']

def exit_app():
    io.save_data(data)
