#!/usr/bin/python3

from  googlsearch import search
import time


urldata=open('/root/Desktop/Python/Python/url.txt','w')
find=input("enter your search data:")
for i in search(find,tld="co.in",stop=10):
	print(i)
	urldata.write(i+"\n")
	time.sleep(2)
urlfind.close()

	
