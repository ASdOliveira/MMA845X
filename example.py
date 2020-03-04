############################################
#
# Practical example of acelerometer library
#
############################################

from acelerometer import *
from time import sleep  #optional import


# Address normally is 0x1D when SA0 is in 3V3
# and is 0x1C when SA0 pin is in GND
acelerometer_address = 0x1D

myAcel = acelerometer(acelerometer_address)

while True:
    myAcel.read()
    print("x = {0}, y = {1}, z = {2}".format(myAcel.x, myAcel.y, myAcel.z))
    print(myAcel.readPosition())
    sleep(0.3)
    
    