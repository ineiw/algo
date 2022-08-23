
def solution(clothes):
    answer = 1
    clothDict = {}
    for i in range(len(clothes)):
        kindOfClothes = clothes[i][1]
        if not kindOfClothes in clothDict:
            clothDict[kindOfClothes] = 1
        else:
            clothDict[kindOfClothes] += 1
    lenKind = len(clothDict)

    for key,val in clothDict.items():
        answer *= (val + 1)
    return answer -1 