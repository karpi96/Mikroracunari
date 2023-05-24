#! /usr/bin/env python

# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import drivers
import time
import random  #randint(a,b)
import RPi.GPIO as GPIO

buttonPin = 17

click = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buttonPin,GPIO.IN)

def button_callback(buttonPin):
    display.lcd_clear()
    display.lcd_display_string("Zdravo", 1)  # Write line of text to first line of display   # Refresh the first
    print("button pressed")

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first

display = drivers.Lcd()
display.lcd_display_string("Dobar dan", 1)

GPIO.add_event_detect(buttonPin, GPIO.RISING, callback = button_callback, bouncetime = 700)


while True:
    time.sleep(0.01)
