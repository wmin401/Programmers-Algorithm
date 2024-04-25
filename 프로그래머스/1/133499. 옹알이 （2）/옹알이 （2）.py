def solution(babbling):
    
    result = 0
    
    for word in babbling:
        for b in ["aya","ye","woo","ma"]:
            if b * 2 not in word:
                word = word.replace(b," ")
                
        if word.isspace():
            result += 1
    
    return result