def __main__():
    n = int(input())
    m = int(input())

    graph = [[] for i in range(n)]
    visited = [False for i in range(n)]
    for i in range(m):
        a,b = map(int,input().split())

        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    print(dfs(0,visited,graph,0))

def dfs(n,visited,graph,depth):
    
    visited[n] = True

    for node in graph[n]:
        if not visited[node]:
            depth = dfs(node,visited,graph,depth+1)

    return depth

__main__()
