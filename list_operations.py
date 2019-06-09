#!/usr/bin/Python3

adhoc=[]
great5=[]
greateq2=[]
n=int(input("enter elements of the list:"))
for i in range(0,n) :
	element=int(input())
	adhoc.append(element)

print("1:print elements greater than 5")
print("2:print elements	greater or equal to 2")
choice=int(input("enter your choice:"))
if choice ==1 :
	for i in range(0,n):
		if adhoc[i] > 5:
			great5.append(adhoc[i])
		else:
			continue

	print("elements greater than 5 are:")
	print(*great5)


elif choice ==2:
	for i in range(0,n):
		if adhoc[i] >= 2 :
			greateq2.append(adhoc[i])
		else:
			continue

	print("elements greater or equal to 2 are:")
	print(*greateq2)



			


