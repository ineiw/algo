datas = []
for i in range(9):
    datas.append(int(input()))

res = 0
result = []
flag = False
for i in range(9):

    for j in range(9):
        res = 0
        result = []
        for k in range(9):
            if not (i == k) and not (j == k) and j!=i:
                result.append(datas[k])
                res += datas[k]
        # print(res)
        if res == 100:
            flag = True
            result.sort()
            for j in result:
                print(j,end=" ")
            break
    if flag :
        break

