from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for permutation in permutations(dungeons, len(dungeons)):
        cnt = 0
        tmp = k
        
        for fatique in permutation:
            if tmp >= fatique[0]:
                tmp -= fatique[1]
                cnt +=1
            
            if cnt > answer:
                answer = cnt
    
    return answer