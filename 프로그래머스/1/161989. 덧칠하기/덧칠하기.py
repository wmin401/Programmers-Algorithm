def solution(n, m, section):
    
    answer, paint = 0, 0
    for i in section:
        if i > paint:
            paint = i + m - 1
            answer += 1
        
        
    return answer