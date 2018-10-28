# examples:
# p = 1020.34         #currently pha
# ambient = 16       # celsius
# speed = 0.61

dragList = []
pressureList = []

#drag formula: 0.5 *
def get_drag(pDry_air, speed):

        A = 2.27     #frontal area coefficent
        Cd = 0.29    #drag coefficient

        AeroDrag = 0.5 * pDry_air * Cd * A * (speed*speed)
        dragList.append(AeroDrag)

def get_pressure(ambient,pressure, speed):

        air_pressure =  pressure * 100          #multiply by 100 to convert from hpa to pa
        tempConstant = ambient + 273.15 #convert to Kelvin
        gasConstant = 287.05            # specific gas constant for dry air
        pDry_air = air_pressure / (tempConstant*gasConstant)
        print('dry air pressure:', pDry_air)
        pressureList.append(pDry_air)
        get_drag(pDry_air, speed)


def prepare_drag(listtemperature, listpressure, speedList):
        for x in range(len(listtemperature)):
            ambient = listtemperature[x]
            pressure = listpressure[x]
            speed = speedList[x][1] * 0.277778  #convert to meter per second
            get_pressure(ambient,pressure,speed)

        return(dragList)

