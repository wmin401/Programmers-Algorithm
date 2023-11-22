def solution(rsp):
    
    solved = {"2":"0","0":"5","5":"2"}
    
    answer = ''
    for i in rsp:
        answer += solved[i]
    return answer