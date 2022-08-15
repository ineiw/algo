import copy
def solution(N, stages):
    approach = [0 for i in range(N+1)]
    notyet = [0 for i in range(N+1)]
    res = []
    for stage in stages:
        for i in range(stage):
            approach[i] += 1
        notyet[stage-1] += 1
    
    for i in range(N):
        if approach[i] == 0:
            res.append(0)
            continue
        a = notyet[i] / approach[i]
        res.append(a)
        
    dicres = {i+1 : res[i] for i in range(len(res))}
    res2 = sorted(dicres.items(), key = lambda item: item[1],reverse=True)
    answer = [i[0] for i in res2]
    
    return answer