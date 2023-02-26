#!/usr/bin/python
import time
import sys
#import RPi.GPIO as GPIO

# function, which starts a programm at a given time every day
# here: function starts start_pumps_fucntion
# input: now, start_time
# output: recursive, starts itself again
def start_programm_function(now, start_time):
	if now == start_time:
		start_pumps_function(duration_min)
		#print("now!")
		time.sleep(60)
		now = time.asctime().split(" ")[3]
		return start_programm_function(now, start_time)
	else:
		now = time.asctime().split(" ")[3]
		#print("now", now)
		time.sleep(60)
		return start_programm_function(now, start_time)

# function, which starts a programm at a given time every day.
# here: at the given time the word "now" with the given time is printed
# input: now, start_time, seconds
# output:
def test(now, start_time, seconds):
	sys.setrecursionlimit(10000)
	if seconds == "0":
		#start_pumps_function(duration_min)
		print("now!", "now:", now)
		time.sleep(1)
		now = time.asctime().split(" ")[3]
		seconds = list(time.asctime().split(" ")[3])[-1]
		return test(now, start_time, seconds)
	else:
		now = time.asctime().split(" ")[3]
		seconds = list(time.asctime().split(" ")[3])[-1]
		print("now", now)
		time.sleep(1)
		return test(now, start_time, seconds)

# function, which aktivates the pumps and stops it after a given time
# input: duration_min
# output: none (pumps starting watering)
#Pumpe 1: 9
#Pumpe 2: 10
#Pumpe 3: 22
#Pumpe 4: 27
#Pumpe 5: 17
def start_pumps_function(duration_min):
	#pass
	pumps = [9,10,22,27,17]
	GPIO.setmode (GPIO.BCM)
	for i in pumps:
		GPIO.setup (i, GPIO.OUT)
		GPIO.output (i, GPIO.LOW)
		time.sleep(duration_min)
		GPIO.output (i, GPIO.HIGH)
	GPIO.cleanup()

# function, which calulates the duration for the needed volume, the needed volume
# is given by the user via input, if not, the last given volume is used
# input:
# output
def duration_min_function():
	#volume_ml = int(input("How many milliliters should be poured? "))
	volume_ml = 300
	duration_min = round(volume_ml/27) #27ml/min
	return duration_min


# function, which asks the user when the programm should start
# if the user does not answer within 10 seconds, the last given time is used
# input:
# output:
def starting_time_function():
#start_time = input("When to start the watering? Please type in format: hh:mm:ss ")
start_time = 07:00:00
return start_time


if __name__ == "__main__":
	#start_time = "22:50:00"
	duration_min = duration_min_function()
	start_time = starting_time_function()
	now = time.asctime().split(" ")[3]
	seconds = list(time.asctime().split(" ")[3])[-1]
	#start_programm_function(now, start_time)
	test(now, start_time, seconds)
