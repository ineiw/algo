import copy
import sys
sys.setrecursionlimit(10**6)
def dfs(visited,cur_color,depth,coordinate,is_overlap):
    s1,s2 = coordinate
    visited[s1][s2] = True
    # print(coordinate,end=" ")
    for a,b in [(0,1),(0,-1),(1,0),(-1,0)]:
        x,y = s1+a,s2+b

        if x < 0  or x >= n or y <0 or y >= n:
            continue
        next_color = ab[x][y]

        if next_color == cur_color and not visited[x][y]:
            dfs(visited,next_color,depth+1,(x,y),is_overlap)
        if (next_color == "R" and cur_color == "G" or next_color =="G" and cur_color =="R") and not visited[x][y] and is_overlap:
            dfs(visited,next_color,depth+1,(x,y),is_overlap)

n = int(input())

ab = []
cnt = 0
cnt2 = 0
visited_of_not_overlap = [[False for i in range(n)] for i in range(n)]
visited_of_overlap = [[False for i in range(n)] for i in range(n)]
for i in range(n):
    ab.append(list(input()))

for i in range(n):
    for j in range(n):
        if not visited_of_not_overlap[i][j]:
            # print(1)
            dfs(visited_of_not_overlap,ab[i][j],0,(i,j),False)
            cnt += 1
        if not visited_of_overlap[i][j]:
            # print(2)
            dfs(visited_of_overlap,ab[i][j],0,(i,j),True)
            cnt2 += 1

print(cnt,cnt2)