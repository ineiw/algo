def ok(minNM,lis,n,m):
    for i in range(minNM,0,-1):
        coc = [0,0,0,0]
        for x in range(n-i+1):
            for y in range(m-i+1):
                
                coc[0] = lis[x][y]
                coc[1] = lis[x+i-1][y]
                coc[2] = lis[x][y+i-1]
                coc[3] = lis[x+i-1][y+i-1]
                prev = coc[0]
                cnt = 1
                for j in coc[1:]:
                    if prev == j:
                        cnt += 1
                        prev = j
                    else:
                        break
                if cnt == 4:
                    return i*i
    return 1

n,m = map(int,input().split())

minNM = min(m,n)
lis = []
for i in range(n):
    lis.append(input())
res = ok(minNM,lis,n,m)
print(res)
