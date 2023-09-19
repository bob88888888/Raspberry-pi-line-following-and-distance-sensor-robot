import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)

GPIO.output(37, False)
GPIO.output(35, False)
try:
    while True:
        GPIO.output(37, True)
        time.sleep(1)
    
        GPIO.output(37, False)
        GPIO.output(35, True)
        time.sleep(1)

        GPIO.output(35, False)
        
finally:
    GPIO.cleanup()
    
    
    