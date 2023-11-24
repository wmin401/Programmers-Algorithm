def solution(my_string):
    answer = ''
    
    for i in my_string:
        if i in ["a", "e", "i", "o", "u"]:
            continue
        answer += i
    return answer