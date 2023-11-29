def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]
    
