#!/usr/bin/python3
import socket

rec=raw_input("enter ip address::")
rec_port=9999

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((rec,rec_port))

while True:
	user=raw_input("enter message::")
	if user=="quit":
		a="server left the chat"
		sock.sendto(str(a),(rec,rec_port))
		info=s.recvfrom(100)
		if info[0]=="client left the chat:"
			print info[0]
			break
		else:	
			print("message from client::"+info[0]")

s.close

