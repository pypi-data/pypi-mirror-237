'''
‘’’#TIME on 7 segment display
Hardware Requirements: Raspberry Pi model 3B+
Power supply
Sd card
Keyboard & Mouse
HDMI cable
Ethernet
HDMI to VGA
Breadboard 
4-digit 7 segment display
Jumper wires (F to F)
(4-digit 7 segment display with IMIG37 controller)

Software Requirements: Raspbian Stretch OS

STEPS:
1.	Connect 4-digit 7 segment display with raspberry pi GPIO pins

IMIG37Board Pin	Function	RPi Physical Pins	Raspberry
GND			Ground		            14			GND
VCC			+5v 		             4			5V
DIO			Data In		            18			GPIO24
CLK			Clock		            16			GPIO23

2.	Download Python script
Create Folder 4digitTime under /home/pi
3.	Commands:
pi@raspberrypi:~/4digitTime $pwd
pi@raspberrypi:~/ $wget https://raspberrytipsn1/files/tm1637.py
pi@raspberrypi:~/4digitTime $ls

4.	Write code to display time

	




CODE:
import sys
import time
import datetime
import RPi.GPIO as GPIO
import tm1637
#CLK->GPIO23(Pin 16)
#DIO->GPIO24(Pin18)
Display=tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL)
Display.Clear()
Display.setBrightness(1)
while(True):
now=datetime.datetime.now()
hour=now.hour
minute=now.minute
second=now.second
currenttime=[int(hour/10),hour%10,int(minute/10),minute%10]
Display.show(currenttime)
Display.showDoublepoint(second%2)
time.sleep(1)

‘’’

'''

def sub(a,b):
    c=a-b
    print(c)