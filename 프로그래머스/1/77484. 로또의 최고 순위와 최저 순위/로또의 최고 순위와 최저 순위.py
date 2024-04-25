def solution(lottos, win_nums): 
    
    rank = [6,6,5,4,3,2,1]
    cnt = lottos.count(0)
    answer = 0
    
    for i in win_nums:
        for j in lottos:
            if i == j:
                answer += 1
    
    return [rank[answer + cnt], rank[answer]]