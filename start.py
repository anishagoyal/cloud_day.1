#!/usr/bin/python

import commands,sys,time,socket,os,getpass

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s_ip="192.168.122.1"
s_port=8888

print "cloud services reloaded..Please enter authentication details"
time.sleep(1)

#to take input for user name
s_user=raw_input("enter the user name: ")

#to take input for user password
print "enter the password"
s_password=getpass.getpass()

s.sendto(s_user,(s_ip,s_port))
s.sendto(s_password,(s_ip,s_port))

s_data=s.recvfrom(2)

if s_data[0] == "ok" :
	print "authentication succesfull!!"
	print "wait for servives!!"
	execfile('saas.py')
	time.sleep(2)

else:
	print "check your user name and password"
	exit()

