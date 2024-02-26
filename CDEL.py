import RPi.GPIO as GPIO


class DEL:
    
    def __init__(self, pin):
        self.__pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        
    def delOn(self):
        GPIO.output(self.__pin, GPIO.HIGH)
        
    def delOff(self):
        GPIO.output(self.__pin, GPIO.LOW)
        
    def cleanUp(self):
        GPIO.cleanup() 
        