from collections import deque
def __main__():
    r,c = map(int,input().split())

    ab = []
    start_j = (0,0)
    start_f_list = []
    for i in range(r):
        ab.append(list(input()))
        for j in range(len(ab[i])):
            if ab[i][j] == "J":
                start_j = (i,j)
            elif ab[i][j] == "F":
                start_f_list.append((i,j))
    print(bfs(start_j,start_f_list,r,c,ab))

def bfs(start_j,start_f,r,c,ab):
    # print(start_j,start_f)
    que = deque()
    s1,s2 = start_j
    que.append((s1,s2,0,"J"))
    for s1,s2 in start_f:
        que.append((s1,s2,0,"F"))
    ok = False
    cnt = 0
    prev_cnt = 0
    while que:

        # print(ab)
        a,b,cnt,whoami = que.popleft()
        
        if whoami == "J" and ab[a][b] == "F":
            continue

        if cnt > prev_cnt:
            prev_cnt = cnt
            if whoami == "F":
                return "IMPOSSIBLE"

        for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
            x = a+i
            y = b+j
            # print(x,y,r,c)
            if x < 0  or x >= r or y < 0 or y >= c:
                if whoami == "J":
                    return cnt+1
                elif whoami == "F":
                    continue
            elif whoami == "J" and ab[x][y] == ".":
                ab[x][y] = "J"
                que.append((x,y,cnt+1,"J"))
            elif whoami == "F" :
                if not ab[x][y] == "#" and not ab[x][y] == "F":
                    ab[x][y] = "F"
                    que.append((x,y,cnt+1,"F"))

    return "IMPOSSIBLE"

__main__()