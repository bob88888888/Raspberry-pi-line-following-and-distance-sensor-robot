import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#IR sernsors
GPIO.setup(21, GPIO.IN)
GPIO.setup(19, GPIO.IN)

#LEDs
GPIO.setup(37, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
    

#LDR
ldr = 40

GPIO.output(37, False)
GPIO.output(35, False)

def rc_time(ldr):
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
    while True:
        value = rc_time(ldr)
        if value >= 8000:
            print ("Lights are off")
            GPIO.output(37, True)
            GPIO.output(35, True)
            
        elif value < 8000:
            print("Lights are on")
            GPIO.output(37, False)
            GPIO.output(35, False)
            
            
        if GPIO.input(21) == True and GPIO.input(19) == True:
            print ("stop")
            
        elif GPIO.input(21):
            print ("left")
            
        elif GPIO.input(19):
            print ("right")
            
        else:
            print ("forward")
            
finally:
    GPIO.cleanup()