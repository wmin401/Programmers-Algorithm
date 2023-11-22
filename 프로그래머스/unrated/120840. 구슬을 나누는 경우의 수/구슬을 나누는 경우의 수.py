def solution(balls, share):
    
    return combination(balls, share)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        
    return result

def combination(n, m):
    return factorial(n) // (factorial(n - m) * factorial(m))