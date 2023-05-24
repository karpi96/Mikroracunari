import RPi.GPIO as GPIO
import time
import drivers


buttonPin1 = 17
buttonPin2 = 15
buttonPin3 = 26
buttonPin4 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buttonPin1,GPIO.IN)
GPIO.setup(buttonPin2,GPIO.IN)

display = drivers.Lcd()

CODE = [2,3,1,4]

inputCode = []

def check():
    global inputCode
    
    if len(CODE) == len(inputCode):
        display.lcd_clear()
        if CODE == inputCode:
            display.lcd_display_string("OK")
        else:
            display.lcd_display_string("STOP")
        inputCode = []

def button1_callback(buttonPin1):
    inputCode.append(1)
    check()
    
def button2_callback(buttonPin2):
    inputCode.append(2)
    check()
    
def button3_callback(buttonPin3):
    inputCode.append(3)
    check()
    
def button4_callback(buttonPin4):
    inputCode.append(4)
    check()

GPIO.add_event_detect(buttonPin1, GPIO.RISING, callback = button1_callback, bouncetime = 700)
GPIO.add_event_detect(buttonPin2, GPIO.RISING, callback = button2_callback, bouncetime = 700)
GPIO.add_event_detect(buttonPin3, GPIO.RISING, callback = button3_callback, bouncetime = 700)
GPIO.add_event_detect(buttonPin4, GPIO.RISING, callback = button4_callback, bouncetime = 700)

while True:
    pass