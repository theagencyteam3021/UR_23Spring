
# Standard Modules
import sys
import math
from time import sleep

# Installed Modules
import rtde_control
import rtde_receive

# Custom Modules
import board # Position Values


# Variables
#==============================================================================
#robotIP = "192.168.59.172"
robotIP = "10.30.21.100"

dropdist = 0.072 # meters of drop and pick


# Initialization
#==============================================================================
rtde_c = rtde_control.RTDEControlInterface(robotIP)
rtde_r = rtde_receive.RTDEReceiveInterface(robotIP)

rtde_c.setPayload(1.330,[.009,.007,.039])




#==============================================================================


# Functions
#==============================================================================
def JointRad(lstDegree):
    lstRad = [math.radians(i)for i in lstDegree]
    return lstRad


def pick(position, board=board):
    print ("Moving to {}".format(position))
    lstJoints = getattr(board, position)
    rtde_c.moveJ(JointRad(lstJoints), 0.5, 0.3)
    target = rtde_r.getActualTCPPose()
    target[2] -= dropdist
    rtde_c.moveL(target) #drop
    sleep(1)
    target[2] += dropdist
    rtde_c.moveL(target) #pick

    # drop 72 mm

    '''
    print("Dropping")
    target = rtde_r.getActualTCPPose()
    print(target)
    target[2] -= 0.10
    print(target)
    sleep(2)
    rtde_c.moveL(target)
    print("Dropped")'''



if __name__ == "__main__":
    print(sys.argv[1])
    # Print joint values as defined in board module
    print(getattr(board, sys.argv[1])) 
    pick(sys.argv[1])
    