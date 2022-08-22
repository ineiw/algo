def solution(phone_book):
    answer = True
    phone_num_dict = {i:0 for i in phone_book}
    for phone_num in phone_book:
        for i in range(len(phone_num)):
            if phone_num[:i] in phone_num_dict:
                return False
    return True