def solution(word):
    return rec(word)

def rec(word):
    word_list = 'AEIOU'
    answer = ''
    cnt = 0
    for i in word_list:
        cnt += 1
        answer += i
        if answer == word:
            return cnt
        for i1 in word_list:
            cnt += 1
            answer += i1
            if answer == word:
                return cnt

            for i2 in word_list:
                cnt += 1
                answer += i2
                if answer == word:
                    return cnt
                for i3 in word_list:
                    cnt += 1
                    answer += i3
                    if answer == word:
                        return cnt
                    
                    for i4 in word_list:
                        cnt += 1
                        answer += i4
                        if answer == word:
                            return cnt
                        answer = answer[:-1]
                        
                    answer = answer[:-1]
                answer = answer[:-1]
            answer = answer[:-1]
        answer = answer[:-1]
        