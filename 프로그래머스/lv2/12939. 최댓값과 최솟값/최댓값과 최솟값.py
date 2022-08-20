def solution(s):
    answer = ''
    maxs = 0
    mins = 10000
    num = ''
    first = True
    s+=' '
    for i in s:
        if i != ' ':
            num += i
        else:
            if first:
                first = False
                maxs = int(num)
                mins = int(num)
                num = ''
                continue
            maxs = max(int(num),maxs)
            mins = min(int(num),mins)
            num = ''
    return str(mins)+" "+str(maxs)