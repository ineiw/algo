def solution(s):
    answer = 0
    s+= ' '
    slen = len(s)
    words = ""
    mins = 1001
    for unit in range(1,slen):
        cnt = 0
        resCnt = 0
        resTring = ''
        prevWords = s[:unit]
        words = ''
        for idx in range(unit,slen):
            word = s[idx]
            words += word
            
            if (idx + 1) % unit == 0 or word == ' ':
                if words == prevWords: # 중복될때
                    cnt += 1
                elif cnt >= 1: # 중복안될때 중복이 있었으면
                    resCnt += len(prevWords) + len(str(cnt+1))
                    resTring += str(cnt+1) + prevWords
                    cnt = 0
                else: # 중복 없었으면
                    resCnt += len(prevWords)
                    resTring += prevWords
                    cnt = 0
                if word == ' ':
                    resCnt += len(words[:-1])
                    resTring += words[:-1]
                        
                prevWords = words
                words = ''
            
                
        # print(resTring,resCnt)
        mins = min(mins,resCnt)
        
    return mins