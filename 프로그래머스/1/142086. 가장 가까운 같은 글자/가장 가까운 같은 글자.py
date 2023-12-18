def solution(s):
    answer = []
    s_dic = {}
    
    for idx, word in enumerate(list(s)):
        if word not in s_dic:
            answer.append(-1)
            s_dic[word] = idx
        else:
            answer.append(idx - s_dic[word])
            s_dic[word] = idx
        
    return answer