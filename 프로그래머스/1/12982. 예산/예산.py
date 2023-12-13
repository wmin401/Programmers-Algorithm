def solution(d, budget):
    
    sorted_list = sorted(d)
    
    cnt = 0
    
    for i in range(len(sorted_list)):
        budget -= sorted_list[i]
        
        if budget < 0:
            return i
        
        cnt = i + 1
   
    
    return cnt