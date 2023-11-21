def solution(my_string, n):
    
    answer = ''
    count = 0
    for i in my_string:
        answer += my_string[count] * n
        count += 1
    return answer