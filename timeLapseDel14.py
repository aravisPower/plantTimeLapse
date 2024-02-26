from CTimeLapse import TimeLapse
import os.path

numberOfPicts = int(input("Nombre de photos à prendre : "))
interval = int(input("Intervalle entre deux photos, en s : "))
pictName = input("Nom du fichier photo (par ex. pict pour pict1, pict2 etc.) : ")
pictType = input("Type de fichier (jpg ou png) : ")
    
directoryName = input("Nom du dossier de stockage des photos : ")
while (os.path.exists(directoryName)):
    directoryName = input("Impossible, il existe déjà ! Donnez un autre nom au dossier de stockage des photos : ")
logFileName = input("Nom du fichier log qui contiendra le nom des photos et les dates/heures de prise de vue (mettre .log en extension) : ")

timeLapse = TimeLapse(numberOfPicts, interval, pictName, pictType, directoryName, logFileName)
timeLapse.start()