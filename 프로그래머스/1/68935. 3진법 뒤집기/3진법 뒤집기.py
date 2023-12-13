def solution(n):
    answer = []
    result = 0
    while n > 0:
        remaindar = n % 3
        n = n // 3
        answer.append(remaindar)
        print(answer)
        
    for i in range(len(answer)):
        result += (3**i) * answer[len(answer) - i - 1] 
        
    
    return result