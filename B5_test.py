#! /usr/bin/env python

# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import drivers
import time
import Adafruit_DHT
import RPi.GPIO as GPIO

grejac = 18
ventilator = 23

dht11 = 4

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(grejac,GPIO.OUT)
GPIO.setup(ventilator,GPIO.OUT)
display = drivers.Lcd()

givenTemp = 25.0
places = "    "

while True:
    # Remember that your sentences can only be 16 characters long!
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,dht11)
    display.lcd_clear()
    display.lcd_display_string(str(temperature) + " , " + str(humidity) , 1)  # Write line of text to first line of display   #
    time.sleep(2)

