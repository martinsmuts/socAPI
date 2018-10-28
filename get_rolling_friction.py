rfList = []
import math
import pandas as pd
import numpy as np
#drag formula: 0.5 *

df = pd.DataFrame()
rfList = []

def get_rollingF(angle): #angle of road in radians

    mass = 1521  #in kg
    rFrac = 0.012   #rolling fraction constant
    grav = 9.81     #gravity constant

    rf = rFrac * mass * math.cos(angle) * grav
    rfList.append(rf)


# elevationList = [[26.0, 26.1, 26.1, 26.1,26.2,26.3,26.2]]
# distList = [0.332, 0.01, 0.273, 0.373, 0.026, 0.048]

elvDiffList = []
elvDiffList_Pos = []
elvDiffList_Neg = []
angleList = []
def get_angle(disList,elvDiffList):

    for x in range(len(elvDiffList)):
         distance = disList[x]*1000 #convert to meters
         rise = elvDiffList[x]
         angle = math.sin(rise/distance)
         get_rollingF(angle)
         angleList.append(angle)


def get_elv_diff(elevationList, distList):
    elevationList_ = []
    elevationList1 = []
    elevationListStart = elevationList[0:-1]
    elevationListEnd = elevationList[1:]

    for x in range(len(elevationListStart)):
        elvStart = elevationListStart[x]
        elvEnd = elevationListEnd[x]
        elvDiffList.append(elvEnd - elvStart)

    get_angle(distList,elvDiffList)

    for x in range(len(elvDiffList)):
        if elvDiffList[x] >= 0:
            elvDiffList_Pos.append(elvDiffList[x])
            elvDiffList_Neg.append(0)
        elif elvDiffList[x] <= 0:
            elvDiffList_Pos.append(0)
            elvDiffList_Neg.append(elvDiffList[x])

    return(rfList, elvDiffList_Pos, elvDiffList_Neg, angleList)







