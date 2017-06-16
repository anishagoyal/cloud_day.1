#!/usr/bin/python

import os,time

x="""
press 1 to open firefox
press 2 to open vlc
press 3 to open open office
press 4 to open screenshot
press 5 to open calculator
press 6 to open webcam
press 7 to open image viewer
press 8 to exit
"""

print x
ch=raw_input()

if ch=='1' :
	print "firefox is about to open"
	time.sleep(2)
	#os.system('firefox')
	execfile('firefox.py')
	#execfile('saas.py')
elif ch=='2' :
	print "vlc is about to open"
	time.sleep(2)
        #os.system('vlc')
	execfile('vlc.py')
	#execfile('saas.py')

elif ch=='3' :
        print "open office is about to open"
        time.sleep(2)
        #os.system('libreoffice')
        execfile('openoffice.py')
        #execfile('saas.py')

elif ch=='4' :
        print "screenshot is now taken"
        time.sleep(2)
        #os.system('gnome-screenshot')
        execfile('screenshot.py')
        #execfile('saas.py')

elif ch=='5' :
        print "calculator is about to open"
        time.sleep(2)
        #os.system('gnome-calculator')
        execfile('calculator.py')
        #execfile('saas.py')

elif ch=='6' :
        print "web camera is about to open"
        time.sleep(2)
        #os.system('cheese')
        execfile('webcam.py')
        #execfile('saas.py')

elif ch=='7' :
        print "image viewer is about to open"
        time.sleep(2)
        #os.system('eog')
        execfile('imageviewer.py')
        #execfile('saas.py')

elif ch=='8':
	exit()

else:
	print "wrong choice"
       
