#!/usr/bin/python3

import datetime

name=input("enter your name::")

cur_time=datetime.datetime.now()
cur_hour=cur_time.hour

if cur_hour < 12:
	print("GOOD MORNING Nigga"+name)
elif cur_hour>=12 and cur_hour<16:
	print("GOOD AFTERNOON Nigga"+name)
elif cur_hour>=16 and cur_hour<=20:
	print("GOOD EVENING Nigga"+name)
else:
	print("GOOD NIGHT Nigga"+name)

