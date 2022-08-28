def solution(w,h):
    answer = 1
    k = 1
    for i in range(min(w,h),0,-1):
        if w%i == 0 and h%i == 0:
            k = i
            break
        
    return w * h - (w + h - k)