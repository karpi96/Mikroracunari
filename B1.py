import RPi.GPIO as GPIO
from gpiozero import LEDCharDisplay
import time
import math
green=14
yellow = 17
red = 15
buttonPin=18

SHORT_DELAY = 0.1 #najmanji delay koji se moze interaptovati
OFF = False #ovo sam napisao samo da bismo lakse razmisljali 
ON = True
status = OFF #trenutno stanje semafora OFF ili ON 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(yellow,GPIO.OUT)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(buttonPin,GPIO.IN, pull_up_down = GPIO.PUD_UP) #pull_up_down je podesen da taster ima vrednost i kad je otkacen



#display1 = LEDCharDisplay(a1,b1,c1,d1,e1,f1,g1) #inicijalizujemo 7 segmentne displeje
#display2 = LEDCharDisplay(a2,b2,c2,d2,e2,f2,g2)


#ovu funkciju koristimo da nam 7 segmentni display odbrojava
#a je broj od kojeg se odbrojava
#b je broj do kojeg se odbrojava (opcionalni parametar, ima vrednost 0 ako ne pisemo nista)
def countDown(a,b = 0):
    global display    
    while a >= b:
        #display1.value = str(math.floor(a/10))
        #display2.value = str(a%10)
        print("prvi broj :" + str(math.floor(a/10)) + "  drugi broj: " + str(a%10)) #ovo je samo da testiram bez displeja
        a-=1
        loop(1)
    
#ovo je sleep funkcija koja se moze interaptovati, i ovo koristimo u programo umesto time.sleep-a 
def loop(sek):
    global SHORT_DELAY
    loops = int(sek/SHORT_DELAY)
    
    for i in range(loops):
        if status == OFF:
            break
        time.sleep(SHORT_DELAY)


#funkcija koja se pozove kad pritisnemo taster
def button_callback(pin1):
    global status
    status = not status

    
#funkcija koja se poziva kad je status == OFF
def button_stop():
    GPIO.output(green,GPIO.LOW)
    GPIO.output(red,GPIO.LOW)
    GPIO.output(yellow,GPIO.LOW)


#ovde vam ide program za semafor
#funkcija koja se vrsi kad je status == ON
def button_start():
    GPIO.output(red, GPIO.HIGH)
    countDown(8)
    GPIO.output(yellow, GPIO.HIGH)
    countDown(2)
    GPIO.output(green, GPIO.HIGH)
    GPIO.output(yellow, GPIO.LOW)
    GPIO.output(red, GPIO.LOW)
    countDown(10,4)
    
    i = 3
    while i > 0:
        print(i)
        #display2.value = str(a%10)
        i-= 1
        GPIO.output(green,GPIO.LOW)
        loop(0.5)
        GPIO.output(green,GPIO.HIGH)
        loop(0.5)
        
    GPIO.output(green,GPIO.LOW)
    
    GPIO.output(yellow, GPIO.HIGH)
    countDown(2)
    GPIO.output(yellow, GPIO.LOW)


#funkcija koja se vrti u beskonacnom ciklusu
def switch():
    global status
    while status == ON:
        button_start()
    while status == OFF:
        button_stop()

#dodamo dogadjaj koji ceka na pritisak tastera
GPIO.add_event_detect(buttonPin, GPIO.RISING, callback = button_callback, bouncetime = 700)


while True:
    switch()


GPIO.cleanup()
        

