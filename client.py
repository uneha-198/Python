#!/usr/bin/python3
import socket

server=raw_input("enter ip address::")
server_port=9999

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((server,server_port))

while True:
	info=sock.recvfrom(100)
	if info[0]=="Server left the conversation":
		print info[0]
		sock.close()
		break
	else:
		print("from server::"+info[0])
  		user=raw_input("enter message to send::")
		if user=="quit": 
			s="client left the chat:"
			sock.sendto(str(a),info[1])
			sock.close()
			break
		else:
			if len(user)>150:
				print("error::limit of characters reached")
			else
				sock.sendto(str(user),data[1])
sock.close
