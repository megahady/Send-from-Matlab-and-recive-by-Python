
''' 
This Code work partially
'''
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import math
import matplotlib.pyplot as plt
import socket
import binascii
import struct 
import socket
import sys
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0",1234))
s.listen(1) 
print("Listening .... \n")
conn, addr = s.accept()
print('Connection address: ', addr)

# data = conn.recv(1024)
# unpackdata=struct.Struct('200h')
# data=struct.unpack('>200h',data) # '>200' is for recieveing 200 short signed point in big-endian form source:https://docs.python.org/3.0/library/struct.html

# x = np.arange(0,len(data)) 

app = QtGui.QApplication([])
win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(1000,900)
win.setWindowTitle('Sensor Data')
pg.setConfigOptions(antialias=True)

# # ==================================
# # Simplest possible plotting example
# pg.setConfigOptions(antialias=True)
# data = np.random.normal(size=1000)
# pg.plot(data, title="Simplest possible plotting example")
# # ==================================


p6 = win.addPlot(title="Updating plot")
curve = p6.plot(pen='y')
ptr = 0
count=0

data = conn.recv(1024)
otr=0
def update():
	global curve, data,ptr
	if len(data)!=0:
		data=struct.unpack('>200h',data) # '>200' is for recieveing 200 short signed point in big-endian form source:https://docs.python.org/3.0/library/struct.html
		curve.setData(data)
		data = conn.recv(1024)
		print(ptr)
		ptr+=1



timer1 = QtCore.QTimer()
timer1.timeout.connect(update)
timer1.start(10) # you can change this refreshment time 


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
