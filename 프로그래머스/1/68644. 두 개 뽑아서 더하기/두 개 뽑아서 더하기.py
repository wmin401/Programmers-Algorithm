from itertools import combinations

def solution(numbers):
    answer = []
    nCr = list(combinations(numbers, 2))
    
    for numSet in nCr:
        answer.append(sum(numSet))
    print(nCr)
    
    return sorted(list(set(answer)))