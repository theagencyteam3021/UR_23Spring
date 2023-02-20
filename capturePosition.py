import rtde_receive
import math
import sys

robotIP = "10.30.21.100"

rtde_r = rtde_receive.RTDEReceiveInterface(robotIP)

#target = rtde_r.getActualQ()

#print (target)

#print([math.degrees(i)for i in target])

if __name__ == "__main__":
    target = rtde_r.getActualQ()
    leeString = ("{} = {}".format(sys.argv[1], [int(math.degrees(i)*100)/100. for i in target] ))
    print(leeString)
    with open("ColePosition.txt", "a") as f:
        f.write(leeString)

    