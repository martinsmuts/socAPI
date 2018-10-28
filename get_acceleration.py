# def get_speedPrevList(speedList, speedLimitList):
    # counter = 0
#     # speedStartList = []
#     # for x in range(len(speedList)):
#     #     if speedList[x][1] < 60 and speedLimit[x][1] <= 70:
#     #         speedStartList.append(0.0)
#     #         counter = counter + 1
#     #         print("counter", counter)
#     #         print(0)
#     #     else:
#     #
#     #         speedPrev = speedList[counter-1][1]
#     #         speedStartList.append(speedPrev)
#     #         counter = counter + 1
#     #         print("counter", counter)
#     #         print(speedList[counter-1][1])
#     # return(speedStartList)


def get_speedPrevList(speedList):
    speedDiffList = []
    speedStartList = speedList[0:-1]
    speedEndList = speedList[1:]

    for x in range(len(speedEndList)):
        speedStart = speedStartList[x][1]
        speedEnd = speedEndList[x][1]
        speedDiffList.append(speedEnd - speedStart)
    return(speedDiffList)

speedList = [['-34.005679,25.66967', 40], ['-34.00004,25.66962', 53], ['-34.00206,25.65548', 48], ['-33.99831,25.65467', 48], ['-33.980317,25.635228', 41]]
durationList = [73, 125, 48, 199]           #remove last item
accList = []

def get_acceleration(speedList, durationList):
    speedDiffListR = get_speedPrevList(speedList)

    for x in range(len(speedDiffListR)):
        speedDiff = speedDiffListR[x] * 0.277778
        duration = durationList[x]
        acc = speedDiff/duration
        accList.append(acc)
    return(accList)






