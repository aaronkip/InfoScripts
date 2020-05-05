#!/bin/python3
import sys
import socket
from datetime import datetime

#Defining target
if len(sys.argv) == 2:
	#Translate Host name to IPV4
	target = socket.gethostbyname(sys.argv[1])
else:
	
