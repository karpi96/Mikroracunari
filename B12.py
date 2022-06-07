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

#promenljiva koji broji klikeve
click = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buttonPin,GPIO.IN, pull_up_down = GPIO.PUD_UP)

#funkcija koja se pozove kad pritisnemo taster
#doda na klik plus 1 i ispise informacije kako je to definisano u zadatku na displej

def button_callback(buttonPin):
    global click
    click += 1
    display.lcd_clear()
    number = random.randint(1,6)
    #ispisi "vas xx broj je xx " u prvom redu
    display.lcd_display_string("vas " + str(click) + " broj je " + str(number), 1) 
    
    #ako dobijemo sesticu ispise u drugom redu "ponovite bacanje"
    if number == 6:
        display.lcd_display_string("Ponovite bacanje", 2)  

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first

display = drivers.Lcd()

#ovaj deo koda radi shiftovanje texta sa leva na desno
#malo sam probao da budem preelegantan moze i da se hardkoduje 

dobro = "Dobro dosli"
i = 0    
while i<=5:
    
    display.lcd_display_string(dobro, 1)
    time.sleep(0.5)
    dobro = " " + dobro
    i += 1
    display.lcd_clear()

#ovo znaci da otkinem prvi karakter sa stringa i izbacim, u ovom slucaju je to space
dobro = dobro[1:]

while i>1:
    dobro = dobro[1:]
    display.lcd_display_string(dobro, 1)
    time.sleep(0.5)
    i -=  1
    display.lcd_clear()




#dodam event na taster
GPIO.add_event_detect(buttonPin, GPIO.RISING, callback = button_callback, bouncetime = 700)

#beskonacna petlja da se ne zavrsi program odmah 
while True:
    time.sleep(0.01)
