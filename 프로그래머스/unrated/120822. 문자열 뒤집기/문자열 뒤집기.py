def solution(my_string):
    
    answer = ""
    count = len(my_string)
    for i in my_string:
        count -= 1
        answer += my_string[count]
    return answer