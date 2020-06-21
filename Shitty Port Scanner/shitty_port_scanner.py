#!/bin/python3
import sys
import socket
from datetime import datetime

#Defining target
if len(sys.argv) == 2:
	#Translate Host name to IPV4
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of arguments")
	print("Syntax: shitty_port_scanner.py <ip>")
	sys.exit()

#Pretty Banner
print("-" * 50)
print("Scanning target " + target)
print("Start Time: "+ str(datetime.now()))
print("-" * 50)
#End Banner
try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #Returns an error indicator
		print("Checking port {}".format(port))
		if result==o:
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting Program")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be ressolved")
	sys.exit()
except socket.error:
	print("Could not connect to server.")
	sys.exit()
