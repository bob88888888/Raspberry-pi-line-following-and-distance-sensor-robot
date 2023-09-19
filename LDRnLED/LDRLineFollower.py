import RPi.GPIO as GPIO
import time


def init():
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setwarnings(False)

    #IR sernsors
    GPIO.setup(21, GPIO.IN)
    GPIO.setup(19, GPIO.IN)

    #LEDs
    GPIO.setup(37, GPIO.OUT)
    GPIO.setup(35, GPIO.OUT)
    
    #motors
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)

    #LDR
    ldr = 40

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
    init
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

def rc_time(ldr, init):
    init
    count = 0
    
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, False)
    time.sleep(0.1)
    
    GPIO.setup(ldr, GPIO.IN)
    
    while GPIO.input(ldr) == 0:
        count += 1
        
    return count
            
#main loop
try:
    init()
    GPIO.output(37, False)
    GPIO.output(35, False)
    while True:
        init()
        value = rc_time(40, init)
                        
        if GPIO.input(21) == True and GPIO.input(19) == True:
            stop(5, init)
            
        elif GPIO.input(21):
            stop(0.1, init)
            right(0.3, init)

            
        elif GPIO.input(19):
            stop(0.1, init)
            left(0.3, init)
            
        else:
            stop(0.01, init)
            forward(0.01, init)
            
        if value >= 45000:
            GPIO.output(37, True)
            GPIO.output(35, True)
            
        elif value < 45000:
            GPIO.output(37, False)
            GPIO.output(35, False)
            
            
finally:
    GPIO.cleanup()