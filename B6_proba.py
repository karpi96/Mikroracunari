import RPi.GPIO as GPIO
import time

buttonPin1 = 18
buttonPin2 = 27
ledPin1 = 17
ledPin2 = 22
ledPin3 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin1,GPIO.OUT)
GPIO.setup(ledPin2,GPIO.OUT)
GPIO.setup(ledPin3,GPIO.OUT)

GPIO.setup(buttonPin1,GPIO.IN)
GPIO.setup(buttonPin2,GPIO.IN)



def button1_callback(buttonPin1):
    GPIO.output(ledPin1, GPIO.HIGH)
    GPIO.output(ledPin2, GPIO.HIGH)
    GPIO.output(ledPin3, GPIO.HIGH)

    
def button2_callback(buttonPin2):
    GPIO.output(ledPin1, GPIO.LOW)
    GPIO.output(ledPin2, GPIO.LOW)
    GPIO.output(ledPin3, GPIO.LOW)

GPIO.add_event_detect(buttonPin1, GPIO.RISING, callback = button1_callback, bouncetime = 700)
GPIO.add_event_detect(buttonPin2, GPIO.RISING, callback = button2_callback, bouncetime = 700)


while True:
    time.sleep(0.01)