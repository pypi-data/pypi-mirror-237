'''
Practical :    control raspberry pi with Telegram
Hardware requirement:
1.	Raspberry Pi model 3B+
2.	LED
3.	Breadboard
4.	Jumper wire
Steps:
1.	Connect 4 lead with raspberry pi’s GPIO pin
2.	Install Telegram App in Mobile. Follow process to obtain access token:
•	Install Telegram app on your Smart Phone from Playstore.
•	Open Telegram.
•	Request the Bot Father to create a new Bot.
•	Search "BotFather" and Click on Start.
•	Create new bot using  /newbot.
•	Provide a Name for your Bot (e.g.msdtyit)
•	Then, Provide username for your Bot
Must be end in "bot" (e.g. msdtyit_bot)
•	 After this process the BotFather will give you
a Token for access

3.	Install Telegram Bot on Raspberry Pi
•	Sudo apt-get update
•	sudo apt-get install python-pip
•	sudo pip install telepot

4.	Write Python Script to blink LED with Telegram Bot :
Program:
import time, datetime
import RPI.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop 

green = 6
yellow = 13
red 19
blue = 26
now = datetime.datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

##LED Blue
GPIO.setup(blue, GPIO.OUT) 
GPIO.output(blue, 0) #Off initially
#LED Yellow
GPIO.setup(yellow, GPIO.OUT)
GPIO.output(yellow, 0) #Off initially
#LED Red
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, 0) #Off initially 
# LED green
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, 0) #Off initially

def action(msg):
chat_id = msg['chat']['id']
command = msg['text']
print ('Received: %s' % command)
If 'on' in command:
message="on"
if 'blue' in command:
message= message + ”blue”
GPIO.output(blue, 1)
if 'yellow' in command: 
message= message + "yellow" 
GPIO.output(yellow, 1)
if 'red' in command:
	message= message+ ”red”
	GPIO.output(red, 1)
if 'green' in command:
message = message + "green “
GPIO.output(green, 1)
if 'all' in command:
message= message + "all"
 		GPIO.output(blue, 1)
GPIO.output(yellow, 1)
GPIO.output(red, 1)
GPIO.output(green, 1)
message = message+ "light(s)"
telegram_bot.sendMessage (chat_id, message)
		if off in command:
			message="off”
			If 'blue' in command:
				message= message +  " blue "
				GPIO.output(blue, 0)
			if 'yellow' in command:
				message= message+ "yellow"
				GPIO.output(yellow, 0)
			if 'red' in command:
				message =message + "red"
				GPIO.output(red, 0)
			If 'green' in command:
				message =message+ "green
				GPIO.output(green, 0)
if 'all' in command:
message= message + "all
GPIO.output(blue, 0)
GPIO.output(yellow, 0) 
GPIO.output(red, 0)
GPIO.output(green, 0)
message =message+ "light(s)"
 			telegram_bot.sendMessage (chat_id, message)
telegram_bot = telepot. Bot(‘  if you want to pass in IOT practical then Enter token key  ’)
print (telegram_bot.getMe())
MessageLoop(telegram_bot, action).run_as_thread()
print ('Up and Running....')
while 1:
time.sleep(10)
for run this program follow this steps: 
	cmd:
	: ~/TelegramLEDdemo $ python telegramled.py











'''

def add8( a, b):
    c=a+b