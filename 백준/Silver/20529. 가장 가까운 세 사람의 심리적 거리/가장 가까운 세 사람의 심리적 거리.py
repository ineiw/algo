import sys

t = int(sys.stdin.readline())

def getDis(mbti1,mbti2):
    dis = 0
    for i in range(4):
        if mbti1[i] != mbti2[i]:
            dis += 1

    return dis

def for3(mbtis,lenMbtis):
    minDis = 100001
    if lenMbtis > 48:
        return 0
    for i1 in range(lenMbtis - 2):
        for i2 in range(i1 + 1,lenMbtis - 1):
            for i3 in range(i2 + 1,lenMbtis):
                mbti1 = mbtis[i1]
                mbti2 = mbtis[i2]
                mbti3 = mbtis[i3]

                dis = getDis(mbti1,mbti2) + getDis(mbti2,mbti3) + getDis(mbti1,mbti3)
                minDis = min(dis,minDis)

    return minDis
totalRes = []
for i in range(t):
    n = int(sys.stdin.readline())
    
    mbtis = sys.stdin.readline().split()
    res = for3(mbtis,n)
    print(res)
#     totalRes.append(res)

# print(totalRes)    
    