
def solution(n):
    answer = 0
    num_list = [True] * (n + 1)
    
    for i in range(2, int(n**0.5 + 1)):
        j = 2
        while i * j <= n:
            num_list[i * j] = False
            j += 1
    
    for i in range(2, n+1):
        if num_list[i]:
            answer += 1
    
    return answer