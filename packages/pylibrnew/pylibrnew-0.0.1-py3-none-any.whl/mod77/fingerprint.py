'''

fingerprint


harware req:
raspebery pi
ethernet
powersupply
fingerprint module
serial usb
jumper wire

pins pin     usb serial
1    5v         5.0v
2    GND        GND
3    txd        rxd
4    rxd        txd
5    touch
6    3.3v


commands:


1.~$sudo bash
2.whoami
3.pwd
4.wget -0-http://apt.pm-codeworks.de/pm-codeworks.de.gppg | apt-key add –
5.apt-get update
6.install python-fingerprint
7.exit
8.whoami
9.pwd
10.ls
11.ls /dev/ttyUSB*
12.cd /usr/share/doc/python-fingerprint/examples/
13.pwd
14.ls
15.sudo python example_index.py
16.clear
17.ls
18.sudo python example_enroll.py
19.sudo python example_search.py
20.ls
21.sudo python example_downloadImage.py





'''

def add3( a, b):
    c=a+b