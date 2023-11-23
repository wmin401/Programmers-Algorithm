def solution(n):
    
    factorial = 1
    i = 0
    while n >= factorial:
        i += 1
        factorial *= i
            
    return i - 1