import sys
from collections import deque

def __main__():
    n,m = map(int,input().split())

    ab = []

    drawing_cnt = 0
    max_drawing = 0

    for i in range(n):
        ab.append(list(map(int,sys.stdin.readline().split())))

    for i in range(n):
        for j in range(m):
            if ab[i][j] == 1:
                drawing_cnt += 1
                v = bfs(i,j,ab,n,m)
                max_drawing = max(max_drawing,v)
                # print(v,(i,j))
    
    print(drawing_cnt)
    print(max_drawing)

def bfs(x,y,ab,n,m):
    que = deque()
    que.append((x,y))
    ab[x][y] = 0
    cnt = 0

    while que:

        a,b = que.popleft()
        cnt += 1

        for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
            x,y = a+i,b+j

            if x >= 0 and x < n and y >= 0 and y < m and ab[x][y] == 1: 
                que.append((x,y))
                ab[x][y] = 0

    return cnt

__main__()