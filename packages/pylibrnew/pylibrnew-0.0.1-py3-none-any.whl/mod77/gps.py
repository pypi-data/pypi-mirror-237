'''
Practical 7 : GPS module interfacing
Hardware requirements:
1. RaspberryPi model 
2. SD card
3. GPS module
4. Jumper Wires (female to female)
5. Breadboard
6. LCD display

GPS board pin:
VCC        1
GND       39
TXD       10
RXD        8

Command:
pi@raspberrypi:~ $  sudo apt-get update
pi@raspberrypi:~ $  sudo apt-get upgrade
pi@raspberrypi:~ $  sudo nano /boot/config.txt
(nano text editor) 
(config.txt already asate tyamadhe fkt ha code add karaycha last la)

-dtoverlay=pi3-disable-bt
-core_freq=250
-enable_uart=1
-force_turbo=1

(press ctrl+x)
Exit


pi@raspberrypi:~ $  sudo cp /boot/cmdline.txt /boot/cmdline.txt.backup
pi@raspberrypi:~ $  sudo nano /boot/cmdline.txt


(nano text editor la gelyanntr console=serial0,115200 kadhun takaych... root=PARTUUID he asel te change karaych root=/dev/mmcblk0p2)
(press ctrl+x)
Exit


pi@raspberrypi:~ $  sudo reboot
pi@raspberrypi:~ $  sudo systemctl stop serial-getty@ttys0.service
pi@raspberrypi:~ $  sudo systemctl disable serial-getty@ttys0.service
pi@raspberrypi:~ $  sudo reboot
pi@raspberrypi:~ $  sudo systemctl enable serial-getty@ttyAMA0.service
pi@raspberrypi:~ $  ls -l /dev
(check for serial->ttyAMA0 in list)
pi@raspberrypi:~ $  sudo apt-get install minicom
pi@raspberrypi:~ $  sudo pip install pynmea2
pi@raspberrypi:~ $  sudo minicom -D/dev/ttyAMA0 -b 9600
(the above same test can also be done using cat command)
pi@raspberrypi:~ $  sudo cat /dev/ttyAMA0




'''

def add4( a, b):
    c=a+b