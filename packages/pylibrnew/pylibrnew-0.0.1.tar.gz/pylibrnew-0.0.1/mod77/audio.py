'''
Practical 8- Record and playback audio on raspberry pi
Hardware requirements:
1. RaspberryPi
2. SD card
3. USB microphone
4. Speaker

Command:

pi@raspberrypi:- $ sudo raspi-config
(Raspberry Pi software configuration tool)
-select advanced option)
-select audio
-(choose audio output) Force 3.5mm ('headphone') jack
-press ok
-finish
pi@raspberrypi:~ $ arecord -l  (used to list available audio input devices)
(Note card number and device number)
pi@raspberrypi:~ $ aplay -l     (used to list available audio output devices)
(Note card number and device number)
pi@raspberrypi:~ $pwd
pi@raspberrypi:~ $nano .asoundrc
(switch to nano editor)
code:
	pcm.!default{
		type asym
		capture.pcm "mic"
		playback.pcm "speaker"
	}
	pcm.mic{
		type plug
		slave{
			pcm "1,0"
		}
	}
	pcm.speaker{
		type plug
		slave{
			pcm "0,0"
		}
	}

****** pcm "<card number><device number>" *******

-press ctrl+x
-save modified buffer?--> yes
-exit

pi@raspberrypi:~ $ nano .asoundrc (continue.......)
pi@raspberrypi:~ $ ls -a
(check for .asoundrc in list)
pi@raspberrypi:~ $ alsamixer (for configuring audio settings)
(press the up arrow key to set playback audio and press ESC to exit)
pi@raspberrypi:~ $ speaker -test -t wav
(press ctrl+c)
pi@raspberrypi:~ $ arecord --format=s16_LE -- duration=5 --rate=16000 --file-type=raw sample.wav
(record audio)
pi@raspberrypi:~ $ $ arecord --format=s16_LE --rate=16000  sample.wav




'''

def add2( a, b):
    c=a+b
    print(c)