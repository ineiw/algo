def solution(A,B):
    answer = 0
    
    ar = sorted(A,reverse=True)
    a = sorted(A)
    br = sorted(B,reverse=True)
    b = sorted(B)
    res1 = 0
    for i in range(len(a)):
        res1 += a[i] * br[i]
    res2 = 0
    for i in range(len(a)):
        res2 += ar[i] * b[i]
    answer = min(res1,res2)
    return answer