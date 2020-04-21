############################################
#
# In this example, we'll obtain the 
# instantaneous acceleration of each axis
# and the board orientation
#
############################################
from library.accelerometer import *
from time import sleep  

# Address normally is 0x1D when SA0 is in 3V3
# and is 0x1C when SA0 pin is connected to GND
accelerometer_address = 0x1C

#instance a new object
myAccel = accelerometer(accelerometer_address)

try:
    while True:
        myAccel.read()
        
        #print the axis acceleration
        print("x = {0}, y = {1}, z = {2}".format(myAccel.x, myAccel.y, myAccel.z))
        
        #print the orientation
        print(myAccel.readPosition())
        sleep(0.3)

#error handling due to keyboard interruption
except KeyboardInterrupt:
    pass    