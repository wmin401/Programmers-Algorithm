def solution(s):
    s_dic = {}
    s_dic =  s_dic.fromkeys(sorted(list(s)),0)
  

    for i in s:
        if i in s_dic.keys():
            s_dic[i] += 1
    answer = ''.join(key for key, value in s_dic.items() if value == 1 )
    return answer