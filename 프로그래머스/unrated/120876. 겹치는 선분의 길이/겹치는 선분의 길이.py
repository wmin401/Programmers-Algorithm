def solution(lines):
    
    sets = [set(range(min(i), max(i))) for i in lines]
    
    return len(sets[0] & sets[1] | sets[1] & sets[2] | sets[0] & sets[2])