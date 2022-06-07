#! /usr/bin/env python

# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import drivers
import time
import Adafruit_DHT
import RPi.GPIO as GPIO

grejac = 14
ventilator = 15

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(grejac,GPIO.OUT)
GPIO.setup(ventilator,GPIO.OUT)
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,17)
display = drivers.Lcd()

givenTemp = 25.0
places = "    "

# Main body of code
try:
    while True:
        # Remember that your sentences can only be 16 characters long!
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,17)
        time.sleep(2)
        display.lcd_clear()
        
        display.lcd_display_string(str(temperature) + " C" + places + str(givenTemp) + " C", 1)  # Write line of text to first line of display   # Refresh the first line of display with a different message
        display.lcd_display_string("Vlaga: " + str(humidity) + "%", 2)  # Write line of text to first line of display   # Refresh the first line of display with a different message
        
        if temperature > givenTemp:
            GPIO.output(ventilator, GPIO.HIGH)
            GPIO.output(grejac, GPIO.LOW)
        
        if temperature < givenTemp:
            GPIO.output(ventilator, GPIO.LOW)
            GPIO.output(grejac, GPIO.HIGH)
            

        # Give time for the message to be read
except KeyboardInterrupt:
    #If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
