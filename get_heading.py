# # -----------------------------------------------------------------------------------------------------------------
# Calculate Bearing
import math
from itertools import tee


def get_heading(LatOrigin, LongOrigin, LatDest, LongDest):
    startLat = math.radians(LatOrigin)
    startLong = math.radians(LongOrigin)
    endLat = math.radians(LatDest)
    endLong = math.radians(LongDest)

    dLong = endLong - startLong

    dPhi = math.log(math.tan(endLat/2.0+math.pi/4.0)/math.tan(startLat/2.0+math.pi/4.0))
    if abs(dLong) > math.pi:
         if dLong > 0.0:
             dLong = -(2.0 * math.pi - dLong)
         else:
             dLong = (2.0 * math.pi + dLong)

    bearing = (math.degrees(math.atan2(dLong, dPhi)) + 360.0) % 360.0;

    return bearing

# pairwise function to be used to iterate through two consecutive rows (pairs) in a dataframe
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

#empty list - will be used to store calculated distances

headingList = [0]

# Loop through each row in the dataframe using pairwise

def prepare_heading_list(list):
        print(list)
        a = list[0:-1]
        b = list[1:]

        for x in range(len(a)):
            LatOrigin = a[x][0]
            LongOrigin = a[x][1]
            LatDest = b[x][0]
            LongDest = b[x][1]

            headingList.append(get_heading(LatOrigin, LongOrigin, LatDest, LongDest))

        return(headingList)


