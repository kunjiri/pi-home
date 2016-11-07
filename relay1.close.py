#!/usr/bin/python
#closes contact on relay1, which is connected to pi's 11

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
while(True):
  GPIO.output(11,GPIO.LOW)
GPIO.cleanup()

