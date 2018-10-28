import math
crosswindList = []
tailwindList = []
headwindList = []

def wind_calc(windDir, windSpeed, heading):
        xwind = 0
        twind = 0
        dirdiff = windDir - heading
        # print(dirdiff)
        if (dirdiff < 0):
            dirdiff = -dirdiff
            print(dirdiff)
        # else:

        xwind = windSpeed * math.sin(0.0174 * dirdiff)

        if(xwind < 0):
            xwind = -xwind
        else:
            if (heading - windDir == 180):
                twind = windSpeed
            else:
                if(windDir - heading == 180):
                    twind = -windSpeed
                else:
                    twind = windSpeed * math.cos(0.0174 * dirdiff)

        print('crosswind:', xwind)
        crosswindList.append(xwind)

        if(twind < 0):
            print('tailwind:' ,twind)
            tailwindList.append(twind)
            headwindList.append(0)
        else:
            print('headwind:', twind)
            headwindList.append(twind)
            tailwindList.append(0)

# # For each row in the column
# for (idx, row) in df.iterrows():
#     windSpeed = (row.windSpeed * 1.94384)   #convert from km/h to knots
#     windDir = row.windBearing
#     heading =  row.heading
#     wind_calc(windDir, windSpeed, heading)

def prepare_wind_type(bearingList, listwindSpeed, listwindBearing):
        for x in range(len(bearingList)):
            windSpeed = listwindSpeed[x] * 1.94384   #convert from km/h to knots
            heading = bearingList[x]
            windDir =  listwindBearing[x]
            wind_calc(windDir, windSpeed, heading)



        return(crosswindList, tailwindList, headwindList)




# listwindSpeed = [2.89, 2.9, 2.9, 2.9, 2.89, 2.89, 2.89, 2.89, 2.88, 2.87, 2.87, 2.82, 2.82, 2.82]
#
# listwindBearing = [101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 101, 100, 100, 100]
#
# bearingList = [0, 90.0, 11.70903153041155, 351.0171461670297, 301.7183408039337, 279.77682886329785, 187.68630300222955, 276.25774414431055, 333.2871329308109, 336.14630488446574, 259.63837437337816, 302.917218675427, 244.88891535887575, 285.44876279012783]
#
# a, b, c = prepare_wind_type(bearingList, listwindSpeed, listwindBearing)
#
# print(a)
# print(b)
# print(c)
