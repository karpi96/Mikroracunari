#! /usr/bin/env python

# Simple string program. Writes and updates strings.
# Demo program for the I2C 16x2 Display from Ryanteck.uk
# Created by Matthew Timmons-Brown for The Raspberry Pi Guy YouTube channel

# Import necessary libraries for communication and display use
import drivers
import time
import Adafruit_DHT
import RPi.GPIO as GPIO

grejac = 14         #pin leda koji simbolizuje grejaca
ventilator = 15     #pin leda koji simbolizuje ventilatora
sensorPin = 17
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(grejac,GPIO.OUT)
GPIO.setup(ventilator,GPIO.OUT)
#iscitavanje vlaznosti i temperature sa DHT11 senzora 
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, sensorPin) 
display = drivers.Lcd()

givenTemp = 25.0
places = "    "

# Main body of code
try:
    while True:
        # Remember that your sentences can only be 16 characters long!
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, sensorPin)
        display.lcd_clear()
        
        #ispisujemo string u prvom redu zato je posle zareza 1
        #moramo da prebacimo sve brojeve u string to znaci str()
        display.lcd_display_string(str(temperature) + " C" + places + str(givenTemp) + " C", 1) 
        display.lcd_display_string("Vlaga: " + str(humidity) + "%", 2)  
        
        #ako je temperature veca od zadate ukljuci ventilator
        if temperature > givenTemp:
            GPIO.output(ventilator, GPIO.HIGH)
            GPIO.output(grejac, GPIO.LOW)
        
        #ako je temperature manja od zadate ukljuci grejac
        if temperature < givenTemp:
            GPIO.output(ventilator, GPIO.LOW)
            GPIO.output(grejac, GPIO.HIGH)

        time.sleep(2)    

except KeyboardInterrupt:
    #kad pritisnete ctr+c onda clearuje display i GPIO
    print("Cleaning up!")
    display.lcd_clear()
    GPIO.cleanup()
