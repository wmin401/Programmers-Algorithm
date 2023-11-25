def solution(order):
    answer = 0
    
    return sum([1 for i in str(order) if int(i) in [3, 6, 9]])