#!/usr/bin/env python3
import controller.controller as c
import service.service as s

'''
This is your main script, this should call several other scripts within your packages.
'''

def main():
	running = True
	while(running):
		c.run_app()


if __name__ == '__main__':
	main()
