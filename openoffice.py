#!/usr/bin/python

import os,socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s_ip="192.168.122.1"
s_port=8888

os.system('ssh -X test@' + s_ip + ' libreoffice4.34.34.34.3')
execfile('saas.py')
