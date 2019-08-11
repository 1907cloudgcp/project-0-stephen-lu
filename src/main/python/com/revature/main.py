#!/usr/bin/env python3
import service.service as s

'''
This is your main script, this should call several other scripts within your packages.
'''
def main():
	s.create_usr("Joe", "test")

if __name__ == '__main__':
	main()
