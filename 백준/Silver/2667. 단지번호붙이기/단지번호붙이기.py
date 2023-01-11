from collections import deque

n = int(input())

graph = []

coordinate_list = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(graph,start,visited):
    cnt = 0
    queue = deque([start])
    cnt += 1
    visited[start[0]][start[1]] = True
    # print(graph)
    while queue:

        v = queue.popleft()
        # print(v)
        for coordinate in coordinate_list:
            x,y = v[0] + coordinate[0] , v[1] + coordinate[1]
            if not (x >= 0 and x < n) or not (y >= 0 and y < n):
                continue
            if not visited[x][y] and graph[x][y] == "1":
                queue.append([x,y])
                visited[x][y] = True
                cnt += 1
    return cnt



def __main__():

    visited = [[False for j in range(n)] for i in range(n)]

    answer = []

    for i in range(n):
        graph.append(input())
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] != "0":
                cnt += 1
                answer.append(bfs(graph,[i,j],visited))
    # print(answer)
    # answer = answer.sort()
    answer.sort()
    print(cnt)
    for i in answer:
        print(i)
__main__()