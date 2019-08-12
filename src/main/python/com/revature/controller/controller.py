from service import service as s
def run_app():
    user = 0
    while (user != '1' and user != '2'):
    	user = input("What would you like to do? (Enter 1 or 2):\n\t1. Register as a new user\n\t2. Login\n")
    	if (user.isdigit()):
    		if (user != '1' and user != '2'):
    			print("Please enter a valid request\n")
    	else:
    		print("Please enter a valid request\n")
    	if (user == '1'):
    		print(s.register_new_usr())
