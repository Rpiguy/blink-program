import RPi.GPIO as GPIO # Importing the GPIO Module
import time # importing the time module

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT) # Setting up GPIO pin 7
GPIO.output(7,0)

try:

    while True: # Creating a never ending loop except if you press CTRL + C
        GPIO.output(7,1) # Turning it on
        time.sleep(1) # Time Delay between on and off
        GPIO.output(7,0) # Turning it off
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
