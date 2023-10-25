'''
Practical  :  Setting Up Wireless Access Point Using Raspberry Pi
Hardware Requirements:
•	A Raspberry Pi Model A/B/B+
•	Ethernet Cable
•	Power Supply for the Pi
•	WiFi USB dongle (Optional)
Software Requirements:
•	Latest Raspbian Stretch OS
•	Putty
•	Advanced IP Scanner Software 
Open cmd:
1.	~ $ Sudo apt-get update
2.	~ $  Sudo apt-get install hostapd
a.	Do you want to continue(y/n): y
3.	~ $  Sudo apt-get install bridge-utils
4.	~ $  sudo nano /etc/hostapd/hostapd.conf
a.	Copy below code and paste after above comment
bridge=br0
interface-wlan0
ssid=gjcIT      #NameOfNetwork
hw_mode=g                 #if not work then put  9
channel=7
country_code=IN
ieee80211n=1
ieee80211d=1
wum enabled=1
auth_algs=1
wpa=2
wpa_passphrase=gurukul1123             #PasswordOfYourNetwork
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
5.	Sudo nano/etc/network/interfaces
a.	Copy below code and paste after above comment
Code:
auto lo
iface lo inet loopback
# Ethernet
auto eth0
allow-hotplug eth0
iface eth0 inet manual
# WiFi
auto wlan0
allow-hotplug wlan0
iface wlan0 inet manual
wireless-power off
#Bridge
auto br0
iface br0 inet dhcp
bridge_ports eth0 wlan0
bridge_fd  0
bridge_stp off
6.	Sudo nano/etc/default/hostapd
RUN_DAEMON=yes
DAEMON_CONF=”/etc/hostapd/hostapd.conf”









'''

def add1( a, b):
    c=a+b
    print(c)