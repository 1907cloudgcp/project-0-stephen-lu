#!/usr/bin/env python3
import service.service as s
import mock

'''
This is your main testing script, this should call several other testing scripts on its own
'''
def main():
		assert s.find_user('emma_j', 'verysecure') == ["Successful login\n",         {
		            "balance": 4500,
		            "first_name": "Emma",
		            "last_name": "Johnson",
		            "password": "verysecure",
		            "transactions": "2019-08-13 23:40:44.830982    Deposit 5000\n2019-08-13 23:40:47.391382    Withdraw 500\n",
		            "user_name": "emma_j"
		        }]
		assert s.find_user('emma_j', 'pass') == ["Incorrect username or password\n"]

		assert s.history({
	"balance": 500,
	"first_name": "Liam",
	"last_name": "Smith",
	"password": "password",
	"transactions": "",
	"user_name": "liam_s"
}) == ''

if __name__ == '__main__':
	main()
