'''
Practical: Interfacing Raspberry with RFID
Hardware Requirements:
•	Raspberry pi Model 3B+
•	RFID Reader (RC522)
•	RFID tags or cards
•	Jumper wire Female to Male
•	Breadboard
 Software Requirements:
•	Raspbian Stretch os
•	SPI supporting library
•	RC522 Python library
 Connection:
RFID reader                        RPI Physical                       Raspberry pi
Board pin                               pin                                 function
SDA                                    24                                     GPIO8
SCK                                    23                                     GPIO11
MOSI                                    19                                    GPIO10
MISO                                     21                                    GPIO9
IRQ                                    unused                           
GND                                      6                                          GND
RST                                     22                                      GPIO25
3.3V                                    1                                        3.3PWR

Commands:
Step 1: updating raspberry pi 
pi@raspberry pi:~$ sudo apt-get update
pi@raspberry pi:~$ sudo raspi-config
select using ArrowKeys->Interface option->SPI->Enable
step 2:
check to make sure that spi has been enabled 
pi@raspberry pi:~$ lsmod |grep spi

step 3:
pi@raspberry pi:~$ sudo apt-get install python2-des python3-pip
pi@raspberry pi:~$ sudo pip3 install spidev
pi@raspberry pi:~$ sudo pip3 install mfrc522

pi@raspberry pi:~$ pwd
/home/pi
pi@raspberry pi:~$ cd rfiddemo/
pi@raspberry pi:~$ pwd
/home/pi/rfiddemo
pi@raspberry pi:~ / rfiddemo $ sudo nano write.py
code:
import RPi.GPIO as GPIO
from mfrc522 import simpleMFRC522
reader=simple MFRC522
print(“looking for cards”)
print(“ press cntr to stop”)
try:
	text=input(“enter new data”)
	print(“now place your tag to write….”)
	reader.write(text)
	print(“data written successfully”)
finally:
	GPIO.cleanup(()
pi@raspberry pi:~ /rfiddemo $ pwd
/home/pi/rfidemo
pi@raspberry pi:~ /rfiddemo $ sudo nano read.py

code:
import RPi.GPIO as GPIO
from mfrc522 import simpleMFRC522
reader=simpleMFRC522C
print(“looking for cards”)
print(“ press cntr to stop”)
try:
	id,text=reader.read()
	print(id)
	print(text)
finally:
	GPIO.cleanup()
pi@raspberry pi:~ /rfiddemo $ sudo python3 read.py
                  


'''

def add7( a, b):
    c=a+b