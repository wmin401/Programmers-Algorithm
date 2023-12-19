def solution(name, yearning, photo):
    answer = []
   
    p_dic = dict(zip(name, yearning))
    print(p_dic)
    
    for pho in photo:
        grade = 0
        for i in pho:
            if i in p_dic:
                grade += p_dic[i]
                
        answer.append(grade)
    
    return answer