HARDWARE USED
1. Raspberry Pi 2, version B
2. Relay, It reads "Songle", 4 channel
3. 2N2222 an npn transistor for switching
4. 10 k resistor

SETUP
1. Pi's gpio 11,13,15,and 19 are connected to Relays through the transistor switching circuit. gpio's are at 3v3, not 5v. However, pi has 5v onboard.

PROGRAM
1. For each relay n, there are 4 files associated
	relayn.close	-bash script that calls relayn.close.py; also kills 
			relayn.open.py if running; in effect closes relay1 
			and holds the satus.
	relayn.close.py-does low level switching.
	relayn.open    -works similar to relayn.close 
	relayn.open.py -wllll similar to relayn.close.py

