def solution(babbling):
    
    language = ["aya", "ye", "woo","ma"]
    cnt = 0
    for word in babbling:
        for say in language:
            word = word.replace(say,"*")
        
        if word == "*" * len(word):
            cnt +=1

    return cnt