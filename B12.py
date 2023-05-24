#! /usr/bin/env python

# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import drivers
import time
import random
import RPi.GPIO as GPIO

buttonPin = 17

click = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buttonPin,GPIO.IN)

def button_callback(buttonPin):
    global click
    print("buttonPressed")
    click += 1
    display.lcd_clear()
    number = random.randint(1,6)
    display.lcd_display_string("vas " + str(click) + " broj je " + str(number), 1)  # Write line of text to first line of display   # Refresh the first line of display with a different message
    
    if number == 6:
        display.lcd_display_string("Ponovite bacanje", 2)  # Write line of text to first line of display   # Refresh the first line of display with a different message

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first

display = drivers.Lcd()

dobro = "Dobro dosli"
i = 0
    
    
while i<=5:
    
    display.lcd_display_string(dobro, 1)
    time.sleep(0.5)
    dobro = " " + dobro
    i += 1
    display.lcd_clear()

dobro = dobro[1:]

while i>1:
    dobro = dobro[1:]
    display.lcd_display_string(dobro, 1)
    time.sleep(0.5)
    i -=  1
    display.lcd_clear()


GPIO.add_event_detect(buttonPin, GPIO.RISING, callback = button_callback, bouncetime = 800)


while True:
    time.sleep(0.01)
