def solution(k, score):
    answer = [score[0]]
    ranking = [score[0]]
    for i in range(1, len(score)):
              
        if len(ranking) < k:
            ranking.append(score[i])
            ranking = sorted(ranking, reverse = True)
            answer.append(ranking[-1])
        elif len(ranking) == k:
            ranking.append(score[i])
            ranking = sorted(ranking, reverse = True)
            ranking.pop()
            answer.append(ranking[-1])
        
        
    
    return answer