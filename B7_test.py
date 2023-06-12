import RPi.GPIO as GPIO
import time
import drivers


buttonPin1 = 17
buttonPin2 = 27
buttonPin3 =  22    
buttonPin4 =  10


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buttonPin1,GPIO.IN)
GPIO.setup(buttonPin2,GPIO.IN)
GPIO.setup(buttonPin3,GPIO.IN)
GPIO.setup(buttonPin4,GPIO.IN)


display = drivers.Lcd()

def button1_callback(buttonPin1):
    display.lcd_clear()
    display.lcd_display_string("1",1)
    print(1)
    
def button2_callback(buttonPin2):
    display.lcd_clear()
    display.lcd_display_string("2",1)
    print(2)
    
def button3_callback(buttonPin3):
    display.lcd_clear()
    display.lcd_display_string("3",1)
    print(3)
    
def button4_callback(buttonPin4):
    display.lcd_clear()
    display.lcd_display_string("4",1)
    print(4)

GPIO.add_event_detect(buttonPin1, GPIO.RISING, callback = button1_callback, bouncetime = 700)
GPIO.add_event_detect(buttonPin2, GPIO.RISING, callback = button2_callback, bouncetime = 700)
GPIO.add_event_detect(buttonPin3, GPIO.RISING, callback = button3_callback, bouncetime = 700)
GPIO.add_event_detect(buttonPin4, GPIO.RISING, callback = button4_callback, bouncetime = 700)

while True:
    pass