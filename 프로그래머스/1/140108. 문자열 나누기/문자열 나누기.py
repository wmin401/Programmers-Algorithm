def solution(s):
    
    answer = 0
    same, different = 0, 0
    
    for i in s:
        if same == different:
            answer += 1
            k = i
        if k == i:
            same += 1
        else:
            different += 1
    return answer