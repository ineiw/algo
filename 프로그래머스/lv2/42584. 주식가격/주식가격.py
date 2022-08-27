def solution(prices):
    answer = []
    stack = []
    cnt = 0
    cntlis = []
    
    stack.append(prices[0])
    cntlis.append(0)
    answer.append(0)
    for price in prices[1:]:
            
        for i in range(len(cntlis)):
            cntlis[i] += 1
            
        cnt = 1
        while len(stack) > 0 and price < stack[-1]:
            # print(answer,stack,cntlis,price,cnt)
            stack.pop()
            while answer[-cnt] != 0:
                cnt += 1            
            
            answer[-cnt] = cntlis.pop()

            
        cntlis.append(0)
        stack.append(price)
        answer.append(0)
        # print(price)
    
    idx = len(prices) - 1
    # print(cntlis,answer)
    while len(cntlis) != 0:
        if answer[idx] == 0:
            answer[idx] = cntlis.pop()
        idx -= 1
    return answer