#! /usr/bash/python3

#import necessary liberaries
import os
import datetime

curage=int(input("enter your current age:"))

#cur_year= os.system("date +"%Y"")
curdatetime = datetime.datetime.now()
curyear=curdatetime.year

print(curyear)
print(curage)
if curage > 95 :
	reqage=curage-95
	reqyear = reqyear - curyear
	print("you were of age 95 in year:"+str(reqyear))
else :
	reqage=95-curage
	reqyear=reqage+curyear
	print("you will be age 95 in year:"+str(reqyear))

#calculate required age year
 #req_age = age - cur_age

# req_year=cur_year+req_age
#print("you will be 95 years old in year:")
#print(req_year)


