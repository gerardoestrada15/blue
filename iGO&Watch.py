import bluetooth
import time
import os


    
while True:    
    print("Checking " + time.strftime("%a, %d %b %Y %H:%M:%S:%mS", time.gmtime()))

    result = bluetooth.lookup_name('DC:B5:4F:08:1A:E2', timeout=5)
    if (result != None):
        print ("Gerardo: in")
    else:
         print ("Gerardo: out")
         #os.system("python /home/pi/Desktop/blue/correo.py")
#t500= E8:1C:AC:1D:85:92
#t=49:FF:76:BF:62:61