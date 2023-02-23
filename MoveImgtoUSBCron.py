import shutil
import time
import os
from emailme import main


# Paths,
imgdir = "/home/bigfella/Desktop/v3/intruder"
Imgsrc = '/home/bigfella/Desktop/v3/intruder/image.jpg'



while True:

#Check if intruder was captured
    checkDir = os.listdir(imgdir)

    if len(os.listdir(imgdir)) != 0:
        main()
        time.sleep(10)
        #Define Pics Label / timestamp of event
        Imgdst = f'/media/bigfella/rpiext/backup/{time.strftime("%d_%m_%Y-%H_%M_%S")}.jpg'
        shutil.move(Imgsrc, Imgdst)
    time.sleep(10)





