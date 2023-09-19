import RPi.GPIO as GPIO
import time
import Tkinter as tk
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

def forward(tf):
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13, True)
    GPIO.output(15, False)
    time.sleep(tf)
    GPIO.cleanup()
    
def backward(tf):
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(15, True)
    time.sleep(tf)
    GPIO.cleanup()
    
def right(tf):
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, True)
    time.sleep(tf)
    GPIO.cleanup()
    
def left(tf):
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, True)
    GPIO.output(15, False)
    time.sleep(tf)
    GPIO.cleanup()
    
def bareRight(tf):
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    time.sleep(tf)
    GPIO.cleanup()
    
def bareLeft(tf):
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, True)
    GPIO.output(15, False)
    time.sleep(tf)
    GPIO.cleanup()
    
def key_input(event):
    print ('Key', event.char)
    key_press = event.char
    sleep_time = 0.030
    
    if key_press.lower() == 'w':
        forward(sleep_time)
        
    elif key_press.lower() == 's':
        backward(sleep_time)
        
    elif key_press.lower() == 'd':
        left(sleep_time)
        
    elif key_press.lower() == 'a':
        right(sleep_time)
        
    elif key_press.lower() == 'e':
        bareLeft(sleep_time)
        
    elif key_press.lower() == 'q':
        bareRight(sleep_time)
        
comand = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()