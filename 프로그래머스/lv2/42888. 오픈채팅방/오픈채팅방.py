def solution(record):
    answer = []
    elcDict = {}
    for elc in record:
        elclist = elc.split()
        inout = elclist[0]
        uid = elclist[1]
        if len(elclist) == 3:
            name = elclist[2]
            elcDict[uid] = name
        
    for elc in record:
        elclist = elc.split()
        inout = elclist[0]
        uid = elclist[1]
        if inout == 'Enter':
            answer.append(elcDict[uid] + '님이 들어왔습니다.')
            
        elif inout == 'Leave':
            answer.append(elcDict[uid] + '님이 나갔습니다.')
    
    return answer