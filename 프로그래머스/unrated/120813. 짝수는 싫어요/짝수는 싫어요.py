def solution(n):
    
    count = []
    
    for i in range(0, n + 1):
        if i % 2 != 0:
            count.append(i)
    
            
    answer = sorted(count)
    return answer