import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(21, GPIO.IN)
GPIO.setup(19, GPIO.IN)

try:
    while True:
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