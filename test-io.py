
# Standard Modules
import sys
import math
from time import sleep

# Installed Modules
import rtde_control
import rtde_receive
import rtde_io

# Custom Modules
import board # Position Values


# Variables
#==============================================================================
#robotIP = "192.168.59.172"
robotIP = "10.30.21.100"

dropdist = 0.072 # meters of drop and pick

# on is closed, off is open --- IO#5


# Initialization
#==============================================================================
rtde_c = rtde_control.RTDEControlInterface(robotIP)
rtde_r = rtde_receive.RTDEReceiveInterface(robotIP)
rtde_io = rtde_io.RTDEIOInterface(robotIP)

rtde_c.setPayload(1.330,[.009,.007,.039])




#==============================================================================


# Functions
#==============================================================================
def JointRad(lstDegree):
    lstRad = [math.radians(i)for i in lstDegree]
    return lstRad


def ioStuff(ioNumber):
    print(rtde_r.getDigitalOutState(ioNumber))
    if rtde_r.getDigitalOutState(ioNumber):
        rtde_io.setStandardDigitalOut(ioNumber, False)


    
if __name__ == "__main__":
    print(sys.argv[1])
    # Print joint values as defined in board module
    ###print(getattr(board, sys.argv[1])) 
    ioStuff(int(sys.argv[1]))
    