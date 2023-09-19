import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

delayTime = 0.1
value = 0#ldr value
ldr = 40
led1 = 37
led2 = 35
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

GPIO.output(led1, False)
GPIO.output(led2, False)
def rc_time(ldr):
    count = 0
    
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, False)
    time.sleep(delayTime)
    
    GPIO.setup(ldr, GPIO.IN)
    
    while GPIO.input(ldr) == 0:
        count += 1
        
    return count

try:
    while True:
        print("LDR Value:")
        value = rc_time(ldr)
        print (value)
        if value >= 5300:
            print ("Lights are off")
            GPIO.output(led1, True)
            GPIO.output(led2, True)
            
        elif value < 5300:
            print("Lights are on")
            GPIO.output(led1, False)
            GPIO.output(led2, False)
            
finally:
    GPIO.cleanup()
            
            
        
    
