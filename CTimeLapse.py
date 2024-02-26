import os
import time
import datetime
from picamera2 import Picamera2
from CDEL import DEL


class TimeLapse:
    
    def __init__(self, numberOfPicts, interval, pictName, pictType, directoryName, logFileName):
        self.__numberOfPicts = numberOfPicts
        self.__interval = interval
        self.__alreadyPicted = 0
        self.__pictName = pictName
        self.__pictType = pictType
        self.__directoryName = directoryName
        if logFileName !='':
            self.__logFileName = logFileName
        else: self.__logFileName = 'datafile.log'
        
        self.__led = DEL(14)
        
        self.picam2 = Picamera2()
        self.picam2.configure("still")
        self.picam2.start()

        # Give time for Aec and Awb to settle, before disabling them
        time.sleep(1)
        self.picam2.set_controls({"AeEnable": False, "AwbEnable": False, "FrameRate": 1.0})
        # And wait for those settings to take effect
        time.sleep(1)
        
    def start(self):
        os.mkdir(self.__directoryName)
        
        for i in range(1, self.__numberOfPicts + 1):
            self.__led.delOn()
            request = self.picam2.capture_request()
            request.save("main", f"{self.__directoryName}/{self.__pictName}{i}.{self.__pictType}")
    
            print(f"Image n°{i} sur {self.__numberOfPicts}")
            #print(r.get_metadata()) # this is the metadata for this image
            request.release()
            self.__led.delOff()
            stringToSave = self.__pictName + str(i) + "." + self.__pictType + ";" + str(datetime.datetime.today().date()) + ";" + str(datetime.datetime.today().time().strftime('%H:%M:%S')) + "\n"
            print(stringToSave)
            # enregistrement de l'historique en format CSV, séparateur ";"
            pathToLogFile = self.__directoryName +"/" + self.__logFileName
            with open(pathToLogFile, 'a') as fichierlog:
                fichierlog.write(stringToSave)
            time.sleep(self.__interval)
        
       self.__led.cleanUp() 
    
    def stop(self):
        pass
    
    def getAlreadyPicted(self):
        return self.__alreadyPicted
    
    
        