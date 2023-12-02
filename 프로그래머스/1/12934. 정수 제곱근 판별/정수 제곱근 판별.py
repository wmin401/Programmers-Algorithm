

def solution(n):
    
    squred_n =  n ** 0.5
    if int(squred_n) == squred_n:
        return (squred_n + 1)**2
    return -1