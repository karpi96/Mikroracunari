import RPi.GPIO as GPIO
import time

#dva tastera
buttonPin1 = 18
buttonPin2 = 27

#tri leda
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

#napravimo da ledovi budu kontrolisani sa PWM
pwm1 = GPIO.PWM(ledPin1,100) #pin 17 na 100Hz
pwm2 = GPIO.PWM(ledPin2,100)
pwm3 = GPIO.PWM(ledPin3,100)

#duty cycle, koliko je sirok puls u procentima
dc = 0

#svaki led pocinje sa 0% znaci ne svetli
pwm1.start(dc)
pwm2.start(dc)
pwm3.start(dc)

#funkcija koju pozovemo kad pritisnemo taster 1 
#doda se na puls 10% sto znaci da ce led jace sijati
def button1_callback(buttonPin1):
    global dc
    global pwm
    dc += 10
    #ovo ne dozvoljava da dc ima visu vrednost od 100% nego se fiksira na 100
    if dc > 100:
        dc = 100
    pwm1.ChangeDutyCycle(dc)
    pwm2.ChangeDutyCycle(dc)
    pwm3.ChangeDutyCycle(dc)

#funkcija koju pozovemo kad pritisnemo taster 2 
#oduzme se od pulsa 10% sto znaci da ce led manje sijati  
def button2_callback(buttonPin2):
    global dc
    global pwm
    dc -= 10
    #ovo ne dozvoljava da dc ode u minus nego ostaje na nuli
    if dc < 0:
        dc = 0
    pwm1.ChangeDutyCycle(dc)
    pwm2.ChangeDutyCycle(dc)
    pwm3.ChangeDutyCycle(dc)


#dogadjaji ili eventi koje se podesavaju na tastere
#uvek citaju taster pored toga sto nam glavni program izvrsava
#bouncetime je vreme u ms, koji nam radi neki debouncing, u principu nece da reaguje na button 700ms zato ne pritiskajte prebrzo
GPIO.add_event_detect(buttonPin1, GPIO.RISING, callback = button1_callback, bouncetime = 700)
GPIO.add_event_detect(buttonPin2, GPIO.RISING, callback = button2_callback, bouncetime = 700)

#beskonacna petlja da nam se program ne zavrsi odmah, jer inace ne bismo mogli ni da pritisnemo dugme on bi zavrsio
while True:
    time.sleep(0.01)
