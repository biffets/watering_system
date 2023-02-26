#!/usr/bin/python

import RPi.GPIO as GPIO
import time


# function, which aktivates the pumps and stops it after a given time
# input: duration_min
# output: none (pumps starting watering)
#Pumpe 1: 9
#Pumpe 2: 10
#Pumpe 3: 22
#Pumpe 4: 27
#Pumpe 5: 17
def start_pumps_function(duration_sec):
	#pass
	pumps = [9,10,22,27,17]
	GPIO.setmode (GPIO.BCM)
	for i in pumps:
		GPIO.setup (i, GPIO.OUT)
		GPIO.output (i, GPIO.LOW)
	time.sleep(duration_sec)
	#time.sleep(2)
	for i in pumps:
		GPIO.output (i, GPIO.HIGH)
	GPIO.cleanup()

# function, which calulates the duration for the needed volume
# input: volume
# output: duration_sec
def duration_sec_function(volume_ml):
	#volume_ml = int(input("How many milliliters should be poured? "))
	duration_sec = (round(volume_ml/54))*60 #54ml/min
	return duration_sec


if __name__ == "__main__":
	volume_ml = 300
	duration_sec = duration_sec_function(volume_ml)
	start_pumps_function(duration_sec)
