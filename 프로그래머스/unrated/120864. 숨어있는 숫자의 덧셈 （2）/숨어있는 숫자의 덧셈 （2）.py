def solution(my_string):
    
    answer = 0
    number = "0"
    for i in my_string:
        if i.isdigit():
            number += i
        else:
            answer += int(number)
            number = "0"
            
    if number != "0":
        answer += int(number)
            

    
    return answer