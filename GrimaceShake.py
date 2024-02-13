
#Import Libraries Here
import time
import sys

timeToSleep = 1

print("\n\nWelcome to InfoTech Center V1.0\n")
time.sleep(timeToSleep)

#Code to have the ellipsis add a dot every .5 seconds
x = 20
ellipsis = 0

while x != 20:
    x += 1
    message = ("Infotech Center Operating System Loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) #\r prints a carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\n0perating System Successfully Booted Up - Retina Scanned - Access Granted")