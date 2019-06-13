#!/usr/bin/python3

#import liberaries required
import os
from gtts import gtts

os.system("touch cmd_data.txt")
cmd=input("enter the command::")
value=os.path.getsize("data.txt")
excode=os.system(cmd+"2>/dev/null")
if excode==0:
	if value==0:
		f=open("cmd_data.txt","w+")
		f.write(cmd+"\n")
		f.close()
	else:
		f=open("cmd_data.txt")
		f.seek(0)
		lines=f.read().split("\n")
		cd=cmd+" "
		if cd in lines:
			t=gTTS(text="dont run the command",lang='en')
			tts.save("cmd.mp3")
			os.system("xdg-open comd.mp3")
		else:
			 pass	
		f.write(cmd+"\n")
		f.close()
else:
	print("incorrect command entered")
	f=open("cmd_data.txt","a+")
	f.write(cmd+"\n")
	f.close()
