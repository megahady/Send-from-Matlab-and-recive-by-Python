#!/usr/bin/env python    

## This code reads and plot 200 short signed point from Matlab TCP/IP transmession ()
# The code not animate or update the matplolib graph
# please refer to my code for using "pyqtgraph"
import numpy as np 
import matplotlib.pyplot as plt  
import binascii
import struct 
import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0",1234))
s.listen(1) 
print("Listening .... \n")


while True:
	conn, addr = s.accept()
	print('Connection address: ', addr)
	data = conn.recv(1024)
	unpackdata=struct.Struct('200h')
	data=struct.unpack('>200h',data) # '>200' is for recieveing 200 short signed point in big-endian form source:https://docs.python.org/3.0/library/struct.html
	x = np.arange(0,len(data)) 

	plt.title("Incoming Data") 
	plt.xlabel('Time (sec)')
	plt.plot(x, data) 
	plt.show() 

conn.close()
print("Connection Closed ")

# # Compute the x and y coordinates for points on a sine curve 

# Plot the points using matplotlib 
