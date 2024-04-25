def solution(participant, completion):
    
    hashDic = {}
    sumHash = 0
    
    
    for i in participant:
        hashDic[hash(i)] = i
        sumHash += hash(i)
    
    for j in completion:
        sumHash -= hash(j)
        
    
        
    return hashDic[sumHash]