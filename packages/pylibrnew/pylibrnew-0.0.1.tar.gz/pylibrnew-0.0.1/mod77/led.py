'''
‘’’#Blinking LED
Hardware Requirements: Raspberry Pi model 3B+
Power supply
Sd card
Keyboard & Mouse
HDMI cable
Ethernet
HDMI to VGA
Breadboard 
LED
10k ohm resistor
2 jumper wires

Software Requirements: Raspbian Stretch OS

STEPS:
1.	Connect +ve terminal of LED with GPIO pin no 7 using jumper wire
2.	Connect -ve terminal of LED with GPIO pin no 9(GND) using jumper wires
3.	Connect resistor between -ve terminal of LED with physical pin no 9
4.	Write script

CODE:
Import RPi.GPIO as GPIO
Import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

For I in range(5):
GPIO.output(7,TRUE)
print(“LED ON”)
time.sleep(1)
GPIO.output(7,FALSE)
print(“LED ON”)
time.sleep(1)

print(“DONE……..”)
GPIO.cleanup()




'''

def add5( a, b):
    c=a+b