def solution(N, stages):
    
    failRate = {}
    people = len(stages)
    
    for i in range(1, N+1):
        if people !=0:
            failRate[i] = stages.count(i)/people
            people = people - stages.count(i)
        else:
            failRate[i] = 0
        
    
    return sorted(failRate, key=lambda x: failRate[x], reverse=True)
        
        
    
    