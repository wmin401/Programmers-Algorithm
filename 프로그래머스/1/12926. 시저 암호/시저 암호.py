def solution(s, n):
    s = list(s)
    print(s)
    answer = []

    for i in s:
        if i.islower():
            answer.append(chr((ord(i) - ord('a') + n)%26 + ord('a')))
                          
        elif i.isupper():
            answer.append(chr((ord(i) - ord('A') + n)%26 + ord('A')))
        
        else:
            answer.append(i)
    
    return "".join(answer)