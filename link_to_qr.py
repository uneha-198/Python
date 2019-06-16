#!/usr/bin/python3

from googlesearch import search
import pyqrcode
import time
import os



find=input("enter data to be searched:")
results=search(find)

j=[]
for i in search(find,stop=3):

	j.append(i) #to store urls taken in a list
	qr=pyqrcode.create(i)
	qr.svg=("qrscan"+i+".svg")
	
	
