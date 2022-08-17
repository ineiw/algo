def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    temp = ''
    for i in new_id:
        if not (i != '-' and i != '_' and i != '.') or i in alpha or i in num:
            temp += i
    new_id = temp
    temp = ''
    prev = ''
    for i in new_id:
        if i == '.' and prev != '.':
            temp += i
        elif i != '.':
            temp += i
        prev = i
    new_id = temp
    temp = ''
    for i in range(len(new_id)):
        cur = new_id[i]
        if (i == 0 or i == len(new_id)-1) and cur == '.':
            continue
        else:
            temp += cur
    new_id = temp
    temp = ''
    if new_id == '':
        new_id+='a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[14] == '.':
            new_id = new_id[:14]
    if len(new_id) <= 2:
        for i in range(3):
            new_id+=new_id[-1]
            if len(new_id) == 3:
                break
    return new_id