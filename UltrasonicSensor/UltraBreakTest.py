import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

def init():

    GPIO.setmode(GPIO.BOARD)

    #motors
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    #Ultrasonic sensor
    GPIO.setup(12, GPIO.OUT)#trig
    GPIO.setup(18, GPIO.IN)#echo
    
def forward(t, init):
    init()
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(15, True)
    time.sleep(t)
    
def backward(t, init):
    init()
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13,True)
    GPIO.output(15, False)
    time.sleep(t)
    
def right(t, init):
    init()
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, True)
    time.sleep(t)
    
def left(t, init):
    init()
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, True)
    GPIO.output(15, False)
    time.sleep(t)
    
def stop(t, init):
    init()
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    time.sleep(t)
    
def distance(init):
    init()
    sig = 0
    nosig = 0
    # Make sure that the trig pin is not activated before running the program
    GPIO.output(12, False)
    
    GPIO.output(12, True)
    time.sleep(0.00001)
    GPIO.output(12, False)
    
    while GPIO.input(18) == 0:
        nosig = time.time()
        
    while GPIO.input(18) == 1:
        sig = time.time()
        
    t1 = sig - nosig
    
    distance = t1 * 17000
    return distance

while True:
    init()
    d = distance(init)
    forward(0.1, init)
    
    if d < 4:
        stop(5, init)
    
    else:
        pass