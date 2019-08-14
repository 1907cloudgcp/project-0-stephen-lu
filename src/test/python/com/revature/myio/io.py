import json

def get_database():
    with open('../../../resources/database.json', 'r') as myFile:
        data = json.load(myFile)
    return data

def save_data(data):
    with open('../../../resources/database.json', 'w') as outFile:
    	json.dump(data, outFile, indent=4, sort_keys=True)
