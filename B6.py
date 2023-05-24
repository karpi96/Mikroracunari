import RPi.GPIO as GPIO
import time

buttonPin1 = 17
buttonPin2 = 15
ledPin1 = 18
ledPin2 = 23
ledPin3 = 24


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin1,GPIO.OUT)
GPIO.setup(ledPin2,GPIO.OUT)
GPIO.setup(ledPin3,GPIO.OUT)

GPIO.setup(buttonPin1,GPIO.IN)
GPIO.setup(buttonPin2,GPIO.IN)

pwm1 = GPIO.PWM(ledPin1,100) #pin 17 na 100Hz
pwm2 = GPIO.PWM(ledPin2,100)
pwm3 = GPIO.PWM(ledPin3,100)
dc = 0
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)


def button1_callback(buttonPin1):
    global dc
    global pwm
    dc += 10
    if dc > 100:
        dc = 100
    pwm1.ChangeDutyCycle(dc)
    pwm2.ChangeDutyCycle(dc)
    pwm3.ChangeDutyCycle(dc)

    
def button2_callback(buttonPin2):
    global dc
    global pwm
    dc -= 10
    if dc < 0:
        dc = 0
    pwm1.ChangeDutyCycle(dc)
    pwm2.ChangeDutyCycle(dc)
    pwm3.ChangeDutyCycle(dc)

GPIO.add_event_detect(buttonPin1, GPIO.RISING, callback = button1_callback, bouncetime = 700)
GPIO.add_event_detect(buttonPin2, GPIO.RISING, callback = button2_callback, bouncetime = 700)


while True:
    time.sleep(0.01)
