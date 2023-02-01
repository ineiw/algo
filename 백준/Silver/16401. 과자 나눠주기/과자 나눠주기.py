m,n = map(int, input().split())

ab = list(map(int, input().split()))

def bin_search(datas,m):
    start = 0
    end = max(datas)
    mid = 0
    target = 0
    cnt = 0
    result = 0
    while start <= end:
        mid = (end + start)//2
        target = 0

        if mid == 0:
            break
        for i in datas:
            target += i//(mid)
        if target >= m:
            result = mid
            start = mid + 1
        else :
            end = mid - 1

    return result

print(bin_search(ab,m))