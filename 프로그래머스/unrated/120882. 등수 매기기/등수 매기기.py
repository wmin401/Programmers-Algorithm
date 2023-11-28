def solution(score):
                                    
    answer = sorted([sum(avg) for avg in score], reverse = True)
        
        
    return [answer.index(sum(k)) + 1 for k in score]