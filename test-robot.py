# https://sdurobotics.gitlab.io/ur_rtde/examples/examples.html



import rtde_control
import rtde_receive

import  math
from time import sleep

robotIP = "192.168.59.172"
#robotIP = "10.30.21.100"

rtde_c = rtde_control.RTDEControlInterface(robotIP)
rtde_r = rtde_receive.RTDEReceiveInterface(robotIP)

#rtde_c.moveL([-0.143, -0.435, 0.20, -0.001, 3.12, 0.04], 0.5, 0.3)


actual_q = rtde_r.getActualQ()
q_degrees = [math.degrees(i) for i in actual_q]
#print(q_degrees)

def JointRad(lstDegree):
    lstRad = [math.radians(i)for i in lstDegree]
    return lstRad



A1=[-41.94, -133.75,  -84.57,  -51.19,  87.45, 189.71]
A8=[148.46,  -42.13,   75.85, -123.14, -90.27, 141.69]
H1=[-43.75,  -99.05, -151.17,  -17.89,  89.40, 351.11]
H8=[157.04,  -76.37,  138.12, -149.49, -89.69, 24.47]

HiDig=[151.77,-84.22,78.50,-85.62,-88.18,25.31]
LoDig=[-37.88,-87.08,-85.74,-97.60,94.33,336.62]


#H1rad = [math.radians(i)for i in H1]
#print(H1rad)

rtde_c.moveJ(JointRad(H1), 0.5, 0.3)
print ("Sleeping")
#sleep(.5)
print ("Moving to A1")
rtde_c.moveJ(JointRad(A1), 0.5, 0.3)
print("Dropping")
target = rtde_r.getActualTCPPose()
print(target)
target[2] -= 0.10
print(target)
sleep(2)
rtde_c.moveL(target)
print("Dropped")

sleep(2)
print ("Moving to A8")
rtde_c.moveJ(JointRad(A8), 0.5, 0.3)
#sleep(5)
print ("Moving to H1")
rtde_c.moveJ(JointRad(H1), 0.5, 0.3)
#sleep(5)
print ("Moving to H8")
rtde_c.moveJ(JointRad(H8), 0.5, 0.3)
