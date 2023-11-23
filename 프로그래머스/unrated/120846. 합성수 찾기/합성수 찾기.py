def solution(n):
    answer = 0
    
    for i in range(4, n + 1):
        if is_composite(i):
            answer += 1
            
    return answer

def is_composite(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
        
        if cnt > 2:
            return True
    
    return False
    
    
    