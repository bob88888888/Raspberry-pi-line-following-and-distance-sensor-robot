import RPi.GPIO as GPIO
import curses
import os #import operating system commands
import time

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(18, GPIO.IN)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

def distance(init):
    init()
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

try:
    init()
    
    while True:
        char = screen.getch()
        if char == ord("q"):
            break
        
        if char == ord('S'):# if user entered capital S
            os.system('sudo shutdown now')#Operating system command: shut down staight away
            
        d = distance(init)
        if d > 15:
            
            if char == curses.KEY_UP:
                GPIO.output(7, True)
                GPIO.output(11, False)
                GPIO.output(13, True)
                GPIO.output(15, False)
            
            elif char == curses.KEY_DOWN:
                GPIO.output(7, False)
                GPIO.output(11, True)
                GPIO.output(13, False)
                GPIO.output(15, True)
                
            elif char == curses.KEY_RIGHT:
                GPIO.output(7, True)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, True)
                
            elif char == curses.KEY_LEFT:
                GPIO.output(7, False)
                GPIO.output(11, True)
                GPIO.output(13, True)
                GPIO.output(15, False)
                
            elif char == 10:
                GPIO.output(7, False)
                GPIO.output(11, False)
                GPIO.output(13, False)
                GPIO.output(15, False)
        else:
            GPIO.output(7, False)
            GPIO.output(11, True)
            GPIO.output(13, False)
            GPIO.output(15, True)
            time.sleep(1)
            
            d = distance(init)
            if d > 15:
                continue
                        
finally:
    curses.nocbreak();screenkeypad(0);curses.echo()
    curses.endwin()
    GPIO.cleanup()
   
   
   
   
