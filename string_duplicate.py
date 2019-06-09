#!/usr/bin/python3


# taking string

string=input("enter the string:")

# forming list 

string_list=[]

str_list=[]
new_str = " "

# converting string into list

for i in range(0, len(string)) :
	string_list.append(string[i])
 
# duplicate value checks

for i in string_list:
	if i not in str_list:
		str_list.append(i)

# print result 

print("resulting string :"+new_str.join(str_list))

