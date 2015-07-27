import RPi.GPIO as GPIO
import time
import logging

class LEDs:
    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger
        GPIO.setmode(GPIO.BOARD)
        #GPIO.setwarnings(False)
        #success LED
        GPIO.setup(13,GPIO.OUT)
        GPIO.output(13,0)
        #Busy LED
        GPIO.setup(7,GPIO.OUT)
        GPIO.output(7,0)
        #fail LED
        GPIO.setup(12,GPIO.OUT)
        GPIO.output(12,0)
        logging.debug("LEDS initialised")
        
    def __enter__(self):
        return self

    def busyOff(self):
        GPIO.output(7,0)

    def orange(self):
        GPIO.output(7,1)

    def green(self):
        self.busyOff();
        for _ in range(6):
            GPIO.output(13,1)
            time.sleep(0.3)
            GPIO.output(13,0)
            time.sleep(0.3)
        self.logger.debug("Flashed success LED")

    def red(self):
        self.busyOff();
        for _ in range(6):
            GPIO.output(12,1)
            time.sleep(0.3)
            GPIO.output(12,0)
            time.sleep(0.3)
        logging.info("Flashed failed LED")
        
    def __exit__(self, type, value, traceback):
        self.logger.debug("lights exited")
        GPIO.cleanup()