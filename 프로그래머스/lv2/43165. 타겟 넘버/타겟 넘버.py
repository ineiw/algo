cnt = 0

def dfs(sums,cur,numbers,target,N):
    global cnt
    if cur == len(numbers):
        if sums == target:
            cnt+=1
        return 
    
    dfs(sums + numbers[cur],cur + 1,numbers,target,N)
    dfs(sums - numbers[cur],cur + 1,numbers,target,N)
    
def solution(numbers, target):
    answer = 0
    dfs(0,0,numbers,target,len(numbers))
    answer = cnt
    return answer