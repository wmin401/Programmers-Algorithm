def solution(numbers, hand):
    answer = ''
    
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
        elif i in [3,6,9]:
            answer += 'R'
        elif hand == 'left' and i in [2,5,8,0]:
            answer += 'L'
        elif hand == 'right' and i in [2,5,8,0]:
            answer += 'R'
    return answer