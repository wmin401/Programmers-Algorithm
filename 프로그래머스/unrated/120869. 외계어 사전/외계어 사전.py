def solution(spell, dic):
    
    for word in dic:
        if not set(spell) - set(word):

            return 1
        
    return 2
