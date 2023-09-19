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
    
    #IR sensors
    GPIO.setup(19, GPIO.IN) #left
    GPIO.setup(21, GPIO.IN) #right
    
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
    
    
    if (GPIO.input(21) == True and GPIO.input(19) == True) or (d < 4):
        stop(1, init)
            
    elif GPIO.input(21):
        stop(0.1, init)
        right(0.3, init)
            
    elif GPIO.input(19):
        stop(0.1, init)
        left(0.3, init)
            
    else:
        stop(0.01, init)
        forward(0.01, init)
        
    GPIO.cleanup()

            
