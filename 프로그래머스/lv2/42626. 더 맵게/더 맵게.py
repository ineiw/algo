import heapq
def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    cnt = 0
    lscov = len(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            answer = cnt
            break
        elif lscov == cnt + 1:
            answer = -1
            break
        min2 = heapq.heappop(scoville)
        
        newScov = min1 + (min2 * 2)
        
        heapq.heappush(scoville,newScov)
        cnt += 1
    return answer