def solution(n):
    answer = ''
    lis = "124"
    k = 20

    while n > 0 :
        if n % 3 == 0:
            n -= 1
            rem = n % 3
            quo = n // 3
            rem +=1
        else:
            rem = n % 3
            quo = n // 3
        n //= 3
        answer = lis[rem-1] + answer
    return answer