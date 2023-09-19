import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.IN)

GPIO.setwarnings(False)

def distance():
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
    GPIO.cleanup()
    return distance
        
print(distance())