def solution(num, k):
    answer = 0
    
    for i in str(num):
        if str(k) == i:
            return str(num).index(i) + 1
    return -1