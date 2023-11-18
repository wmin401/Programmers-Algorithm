def solution(array):
    count = [0] * (max(array) + 1)
    print(max(array))
    print(len(array))
    print(count)
    
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
