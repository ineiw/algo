from collections import deque

def bfs(maps,start,visited):
    res = 0
    que = deque()
    que.append(start)
    visited.add(start)
    
    while que:
        node = que.popleft()
        value = maps[node[0]][node[1]]
        res += int(value)
        
        for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
            x,y = node[0] + a,node[1] + b
            
            if not (x >= 0 and x < len(maps)) or not (y >= 0 and y < len(maps[0])):
                continue               
                
            if (x,y) in visited:
                continue
            
            if maps[x][y] == 'X':
                continue 
            
            que.append((x,y))
            visited.add((x,y))
            

    return res,visited

def solution(maps):
    answer = []
    visited = set()
    maps = [list(i) for i in maps]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if (i,j) not in visited and (maps[i][j] != 'X'):
                res,visited = bfs(maps,(i,j),visited)
                answer.append(res)
            
    if not answer:
        answer.append(-1)
    
    return sorted(answer)