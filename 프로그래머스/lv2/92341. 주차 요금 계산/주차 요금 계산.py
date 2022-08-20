import math
def cusTime(time):
    time = time.split(":")
    return int(time[0]) * 60 + int(time[1])

def parkingFeeCalc(fees,durTime):
    return fees[1] + math.ceil((durTime - fees[0]) / fees[2]) * fees[3]
    
def solution(fees, records):
    answer = []
    carDict = {}
    for record in records:
        splitRecord = record.split()
        if splitRecord[-1] == 'IN':
            if splitRecord[1] in carDict:
                sumCarTime = carDict[splitRecord[1]][0] - cusTime(splitRecord[0])
                carDict[splitRecord[1]] = [sumCarTime,"IN"]
            else:
                carDict[splitRecord[1]] = [-cusTime(splitRecord[0]),"IN"]
        elif splitRecord[-1] == 'OUT':
            durTime = cusTime(splitRecord[0]) + carDict[splitRecord[1]][0]
            carDict[splitRecord[1]] = [durTime,"OUT"]
            
    carDict = sorted(carDict.items(), key = lambda item: item[0])
    
    for carName,carData in carDict:
        if carData[1] == "IN":
            sumOfParkingTime = carData[0] + cusTime("23:59")
            if sumOfParkingTime <= fees[0]:
                res = fees[1]
            else:
                res = parkingFeeCalc(fees,sumOfParkingTime)
            answer.append(res)
            
        else:
            sumOfParkingTime = carData[0]
            if sumOfParkingTime <= fees[0]:
                res = fees[1]
            else:
                res = parkingFeeCalc(fees,sumOfParkingTime)
            answer.append(res)
    return answer