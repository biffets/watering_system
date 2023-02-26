#!/usr/bin/python

import time
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)

# Pumpe 1
GPIO.setup (9, GPIO.OUT)
GPIO.output (9, GPIO.LOW)

time.sleep(1)

GPIO.output (9, GPIO.HIGH)

#Pumpe 2
GPIO.setup (10, GPIO.OUT)
GPIO.output (10, GPIO.LOW)

time.sleep(1)

GPIO.output (10, GPIO.HIGH)

#Pumpe 3
GPIO.setup (22, GPIO.OUT)
GPIO.output (22, GPIO.LOW)

time.sleep(1)

GPIO.output (22, GPIO.HIGH)

#Pumpe 4
GPIO.setup (27, GPIO.OUT)
GPIO.output (27, GPIO.LOW)

time.sleep(1)

GPIO.output (27, GPIO.HIGH)

#Pumpe 5
GPIO.setup (17, GPIO.OUT)
GPIO.output (17, GPIO.LOW)

time.sleep(1)

GPIO.output (17, GPIO.HIGH)
GPIO.cleanup()
