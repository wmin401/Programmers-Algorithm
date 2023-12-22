def solution(k, m, score):
    
    sorted_score =  sorted(score)
    result = 0
    for i in range(len(sorted_score)//m):
        box = []
        for j in range(m):
            box.append(sorted_score.pop())
        result += min(box) * m
            
            
        
  
    return result