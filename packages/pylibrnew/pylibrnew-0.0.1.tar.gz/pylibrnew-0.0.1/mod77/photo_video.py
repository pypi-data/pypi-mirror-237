'''
Practical : capture image and videos
Setps:
1.	Connect camera to raspberry pi
2.	Run commands :
•	~ $ sudo apt-get install python-picamera
•	~ $ sudo apt-get install python3-picamera
•	~ $ sudo pip install picamera
 	To Enable camera :
•	~ $ Sudo raspi-config
o	select interfacing option -> select camera -> To enable select = yes  ->     ok  ->   finish  -> to reboot select  = yes
3.	write python code :
1. Capture image:
program:
	#program to capture image starts 
import time
import picamera
camera =picamera.PiCamera() 
camera.resolution =(1024,768)
camera.start_preview()
camera.hflip=True  #horizontal
camera.vflip=True  #vertical
time.sleep(5)
camera.capture('test.jpg')   # file name
camera.stop_preview()
#program to capture image ends
# you can run on direct IDLE 
	2.video:
		Program:
			#program to capture video starts
import picamera
camera =picamera.PiCamera()
camera.resolution (640, 480)
camera.start_recording ('test_video.h264') 
camera.wait_recording (10) 
camera.stop_recording() 
print('finished')
 #program to capture video ends


######     Thank  you   ######








'''

def add6( a, b):
    c=a+b