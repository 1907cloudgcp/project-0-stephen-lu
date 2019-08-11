import json
import io as io


def create_usr(name, password):
    usr_name = name.lower()

    usr = {'name': usr_name, 'password': password, 'transactions': '', 'balance': 0}
    json_usr = json.dumps(usr, indent = 4)
    f = open("../../../resources/database.json", "a")
    f.write(json_usr)
    f.close()

def check_usr(name, password):
    # needs work
    return None
