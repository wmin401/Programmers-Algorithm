def solution(array):
    count = [0] * (len(array) + 1)
    
    for i in array:
        count[i] += 1
        
    m = 0
    
    for i in count:
        if i == max(count):
            m += 1
    
    if m > 1:
        return -1
    else:
        return count.index(max(count))
