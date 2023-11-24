def solution(n):
    squared = int(n ** 0.5)
    
    if squared ** 2 == n:
        return 1
    else:
        return 2