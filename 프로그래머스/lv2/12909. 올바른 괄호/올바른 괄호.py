def solution(s):
    answer = False
    q = []
    for i in s:
        if i == '(':
            q.append(i)
        else:
            if len(q) == 0:
                return False
            elif q[-1] != '(':
                return False
            q.pop()
    if len(q) == 0:
        answer = True
    return answer